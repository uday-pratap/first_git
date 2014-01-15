/**
 * \file     test_parser.c
 * \brief    Test program for parser library. 
 * \details  This is a test program with a simple CLI that serves as a demo 
 *           as well.
 */
#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <string.h>
#include <unistd.h>
#include "cparser.h"
#include "cparser_priv.h"
#include "cparser_token.h"
#include "cparser_tree.h"

/** Zeroize a data structure */
#define BZERO_OUTPUT memset(output, 0, sizeof(output)); output_ptr = output

extern char output[2000], *output_ptr;
extern int interactive;
int num_passed = 0, num_failed =0;

/**
 * \brief    Entry point of the program.
 *
 * \param    argc Number of arguments.
 * \param    argv An array of argument strings.
 *
 * \return   Return 0.
 */
int
main (int argc, char *argv[])
{
    cparser_t parser;
    char *config_file = NULL;
    int debug = 0;

    memset(&parser, 0, sizeof(parser));
    interactive = 1;
    parser.cfg.root = &cparser_root;
    parser.cfg.ch_complete = '\t';
    /* 
     * Instead of making sure the terminal setting of the target and 
     * the host are the same. ch_erase and ch_del both are treated
     * as backspace.
     */
    parser.cfg.ch_erase = '\b';
    parser.cfg.ch_del = 127;
    parser.cfg.ch_help = '?';
    parser.cfg.flags = (debug ? CPARSER_FLAGS_DEBUG : 0);
    strcpy(parser.cfg.prompt, "SSR_UT_AUTOMATION : $  ");
    parser.cfg.fd = STDOUT_FILENO;
    cparser_io_config(&parser);

    if (CPARSER_OK != cparser_init(&parser.cfg, &parser)) {
        printf("Fail to initialize parser.\n");
	return -1;
    }
    if (interactive) {
        if (config_file) {
            (void)cparser_load_cmd(&parser, config_file);
        }
        cparser_run(&parser);
    } 
else {
        /* Run the scripted tests */
    }
    return 0;
}
