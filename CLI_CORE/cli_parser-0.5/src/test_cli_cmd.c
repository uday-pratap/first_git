/**
 * \file     test_parser.c
 * \brief    Test program for parser library. 
 * \details  This is a test program with a simple CLI that serves as a demo 
 *           as well.
 */

#include <assert.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include "cparser.h"
#include "cparser_token.h"

int interactive = 0;
#define PRINTF(args...)                                 \
    if (interactive) {                                  \
        printf(args);                                   \
    } else {                                            \
        output_ptr += sprintf(output_ptr, args);        \
    }

#define MAX_NAME        (128)
#define MAX_EMPLOYEES   (100)
#define MAX_TITLE       (32)

char *output_ptr;
char output[2000]; /* buffer for sprintf */


typedef struct TC_list {
    char tc_name[25];
    uint32_t repeat;
}TC_LIST;

typedef struct cli_py_object {
    uint32_t    ssr_no;
    char        Device_name[25];
    uint32_t    ip_address;
    uint32_t    slot_number;
    char        prompt_name[25];
    TC_LIST     tc[100];
    char        *Expect_input;
}CLI_OBJ;


CLI_OBJ cli_py_obj;



#define perl_command snprintf(command_buf, sizeof(command_buf), "perl Bios.pl %lu %s %lu %lu %s %s %lu %s",\
                               (unsigned long)cli_py_obj.ssr_no,\
                                cli_py_obj.Device_name,\
                               (unsigned long)cli_py_obj.ip_address,\
                               (unsigned long)cli_py_obj.slot_number,\
                                cli_py_obj.prompt_name,\
                                cli_py_obj.tc[0].tc_name,\
				(unsigned long)cli_py_obj.tc[0].repeat,\
				cli_py_obj.Expect_input\
                               );\
			printf("===>%s\n",command_buf);\
                        system(command_buf);


cparser_result_t
cparser_cmd_ssr_Number_rpsw2_console_ip_ipv4_ofw_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	cparser_context_t *context,
        uint32_t *ssr_no, uint32_t *ipv4, char **field, uint32_t *rval, char **Expect)
{	
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"rpsw2");
        cli_py_obj.ip_address = *((uint32_t *)ipv4);
        cli_py_obj.slot_number = 0;
        strcpy(cli_py_obj.prompt_name,"rp-ofw");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
		 cli_py_obj.tc[0].repeat = 0;
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
                strcpy(cli_py_obj.tc[0].tc_name,*field);
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
        }
	   
        perl_command;
        free(cli_py_obj.Expect_input);	
	return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_rpsw2_console_ip_ipv4_shell_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	cparser_context_t *context,
        uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"rpsw2");
        cli_py_obj.ip_address = *((uint32_t *)ipv4);
        cli_py_obj.slot_number = 0;
        strcpy(cli_py_obj.prompt_name,"rp-shell");
        if(field == NULL){
		 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
		 cli_py_obj.tc[0].repeat =0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
                strcpy(cli_py_obj.tc[0].tc_name,*field);

		if(strcmp(*field,"TC_1-2-a1") == 0) {
                  strcpy(cli_py_obj.tc[0].tc_name,"TC_1-2-10");
                }else if(strcmp(*field,"TC_1-2-a2") == 0) {
                  strcpy(cli_py_obj.tc[0].tc_name,"TC_1-2-11");
                }
		if(rval != NULL) {
			cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
		}else {
			cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
		}
        }
        perl_command;
	free(cli_py_obj.Expect_input);
	return CPARSER_OK;
}


cparser_result_t
cparser_cmd_ssr_Number_rpsw2_console_ip_ipv4_ipos_field_Repeat_repeat_value_Expect_Enter_Expect_input(
        cparser_context_t *context,
        uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"rpsw2");
        cli_py_obj.ip_address = *((uint32_t *)ipv4);
        cli_py_obj.slot_number = 0;
        strcpy(cli_py_obj.prompt_name,"rp-ipos");
        if(field == NULL){
		 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
		 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		if(rval != NULL) {
			cli_py_obj.tc[0].repeat = *((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
		}else {
			cli_py_obj.tc[0].repeat =0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
		}
                strcpy(cli_py_obj.tc[0].tc_name,*field);
        }
        perl_command;
        free(cli_py_obj.Expect_input);
        return CPARSER_OK;
}


cparser_result_t
cparser_cmd_ssr_Number_rpsw1_console_ip_ipv4_ofw_field_Repeat_repeat_value_Expect_Enter_Expect_input(
        cparser_context_t *context,
        uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"rpsw1");
        cli_py_obj.ip_address = *((uint32_t *)ipv4);
        cli_py_obj.slot_number = 0;
        strcpy(cli_py_obj.prompt_name,"rp-ofw");
        if(field == NULL){
		 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
		 cli_py_obj.tc[0].repeat = 0 ;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		if(rval !=NULL) {
		  cli_py_obj.tc[0].repeat = *((int*)rval);
                  if(Expect && *Expect) {
                      cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                      strcpy(cli_py_obj.Expect_input,*Expect);
                  }else{
                      cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                      strcpy(cli_py_obj.Expect_input,"NILL");
                 }
		}else {
		   cli_py_obj.tc[0].repeat = 0;
                   cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                   strcpy(cli_py_obj.Expect_input,"NILL");
		}
                strcpy(cli_py_obj.tc[0].tc_name,*field);
        }
        perl_command;
	free(cli_py_obj.Expect_input);
        return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_rpsw1_console_ip_ipv4_shell_field_Repeat_repeat_value_Expect_Enter_Expect_input(
        cparser_context_t *context,
        uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"rpsw1");
        cli_py_obj.ip_address = *((uint32_t *)ipv4);
        cli_py_obj.slot_number = 0;
        strcpy(cli_py_obj.prompt_name,"rp-shell");
        if(field == NULL){
		 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
		 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		strcpy(cli_py_obj.tc[0].tc_name,*field);
		if(strcmp(*field,"TC_1-2-a1") == 0) {
		  strcpy(cli_py_obj.tc[0].tc_name,"TC_1-2-10");
		}else if(strcmp(*field,"TC_1-2-a2") == 0) {
                  strcpy(cli_py_obj.tc[0].tc_name,"TC_1-2-11");
		}
		if(rval !=NULL){
			cli_py_obj.tc[0].repeat = *((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
		}else {
			cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
		}
        }
        perl_command;
        free(cli_py_obj.Expect_input);
        return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_rpsw1_console_ip_ipv4_ipos_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	cparser_context_t *context,
	uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"rpsw1");
        cli_py_obj.ip_address = *((uint32_t *)ipv4);
        cli_py_obj.slot_number = 0;
        strcpy(cli_py_obj.prompt_name,"rp-ipos");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
                strcpy(cli_py_obj.tc[0].tc_name,*field);
        }
        perl_command;
        free(cli_py_obj.Expect_input);
        return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_ssc1_v2_slot_slot_number_efi_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	cparser_context_t *context,
	uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"ssc1-v2");
        cli_py_obj.ip_address = 0 ;
        cli_py_obj.slot_number = *((uint32_t *)ipv4);
        strcpy(cli_py_obj.prompt_name,"ssc-efi");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		strcpy(cli_py_obj.tc[0].tc_name,*field);
                if(strcmp(*field,"TC_2-2-a0")==0) {
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-10");
                }else if(strcmp(*field,"TC_2-2-a1")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-11");
                }else if(strcmp(*field,"TC_2-2-a2")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-12");
                }else if(strcmp(*field,"TC_2-2-a3")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-13");
                }else if(strcmp(*field,"TC_2-2-a4")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-14");
                }
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
			if(Expect && *Expect) {
			   cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
			   strcpy(cli_py_obj.Expect_input,*Expect);
			}else{
			   cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
			   strcpy(cli_py_obj.Expect_input,"NILL");
			}
                }else {
                        cli_py_obj.tc[0].repeat = 0;
			cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
			strcpy(cli_py_obj.Expect_input,"NILL");
                }
	
        }
        perl_command;

	free(cli_py_obj.Expect_input);
	return CPARSER_OK;
}


cparser_result_t
cparser_cmd_ssr_Number_ssc1_v2_slot_slot_number_shell_field_Repeat_repeat_value_Expect_Enter_Expect_input( 
	cparser_context_t *context,
        uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{	
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"ssc1-v2");
        cli_py_obj.ip_address = 0 ;
        cli_py_obj.slot_number = *((uint32_t *)ipv4);
        strcpy(cli_py_obj.prompt_name,"ssc-shell");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		strcpy(cli_py_obj.tc[0].tc_name,*field);
                if(strcmp(*field,"TC_2-1-a")== 0){
                        strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-1");
                }else if(strcmp(*field,"TC_2-1-b")==0){
                        strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-2");
                }else if(strcmp(*field,"TC_2-1-c")==0){
                         strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-3");
                }else if(strcmp(*field,"TC_2-1-d")==0){
                        strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-4");
                }else if(strcmp(*field,"TC_2-1-e")==0) {
                         strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-5");
                }
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
        }
        perl_command;
        free(cli_py_obj.Expect_input);
	return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_ssc2_a_slot_slot_number_efi_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	cparser_context_t *context, 
	uint32_t *ssr_no,uint32_t *ipv4,char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"ssc2-a");
        cli_py_obj.ip_address = 0 ;
        cli_py_obj.slot_number = *((uint32_t *)ipv4);
        strcpy(cli_py_obj.prompt_name,"ssc-efi");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{

		strcpy(cli_py_obj.tc[0].tc_name,*field);
                if(strcmp(*field,"TC_2-2-a0")==0) {
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-10");
                }else if(strcmp(*field,"TC_2-2-a1")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-11");
                }else if(strcmp(*field,"TC_2-2-a2")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-12");
                }else if(strcmp(*field,"TC_2-2-a3")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-13");
                }else if(strcmp(*field,"TC_2-2-a4")==0){
                   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-14");
                }
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
        }
        perl_command;
        free(cli_py_obj.Expect_input);
	return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_ssc2_a_slot_slot_number_shell_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	 cparser_context_t *context,uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{

	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"ssc2-a");
        cli_py_obj.ip_address = 0 ;
        cli_py_obj.slot_number = *((uint32_t *)ipv4);
        strcpy(cli_py_obj.prompt_name,"ssc-shell");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		strcpy(cli_py_obj.tc[0].tc_name,*field);
                if(strcmp(*field,"TC_2-1-a")== 0){
                        strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-1");
                }else if(strcmp(*field,"TC_2-1-b")==0){
                        strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-2");
                }else if(strcmp(*field,"TC_2-1-c")==0){
                         strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-3");
                }else if(strcmp(*field,"TC_2-1-d")==0){
                        strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-4");
                }else if(strcmp(*field,"TC_2-1-e")==0) {
                         strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-5");
                }
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
        }
        perl_command;
        free(cli_py_obj.Expect_input);
	return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_ssc1_slot_slot_number_efi_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	 cparser_context_t *context,uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"ssc1");
        cli_py_obj.ip_address = 0 ;
        cli_py_obj.slot_number = *((uint32_t *)ipv4);
        strcpy(cli_py_obj.prompt_name,"ssc-efi");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		strcpy(cli_py_obj.tc[0].tc_name,*field);
		if(strcmp(*field,"TC_2-2-a0")==0) {
	       	   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-10");
		}else if(strcmp(*field,"TC_2-2-a1")==0){
		   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-11");
		}else if(strcmp(*field,"TC_2-2-a2")==0){
		   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-12"); 
		}else if(strcmp(*field,"TC_2-2-a3")==0){
		   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-13");
		}else if(strcmp(*field,"TC_2-2-a4")==0){
		   strcpy(cli_py_obj.tc[0].tc_name,"TC_2-2-14");
		}
	
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
        }
        perl_command;
        free(cli_py_obj.Expect_input);
        return CPARSER_OK;
}

cparser_result_t
cparser_cmd_ssr_Number_ssc1_slot_slot_number_shell_field_Repeat_repeat_value_Expect_Enter_Expect_input(
	cparser_context_t *context,uint32_t *ssr_no, uint32_t *ipv4, char **field,uint32_t *rval,char **Expect)
{
	char command_buf [2000];
        assert(context);
        cli_py_obj.ssr_no     = *((uint32_t *)ssr_no);
        strcpy(cli_py_obj.Device_name,"ssc1");
        cli_py_obj.ip_address = 0 ;
        cli_py_obj.slot_number = *((uint32_t *)ipv4);
        strcpy(cli_py_obj.prompt_name,"ssc-shell");
        if(field == NULL){
                 strcpy(cli_py_obj.tc[0].tc_name,"NILL");
                 cli_py_obj.tc[0].repeat = 0;
                 cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                 strcpy(cli_py_obj.Expect_input,"NILL");
        }else{
		strcpy(cli_py_obj.tc[0].tc_name,*field);
		if(strcmp(*field,"TC_2-1-a")== 0){
			strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-1");
		}else if(strcmp(*field,"TC_2-1-b")==0){
			strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-2");
		}else if(strcmp(*field,"TC_2-1-c")==0){
			 strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-3");
		}else if(strcmp(*field,"TC_2-1-d")==0){
			strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-4");
		}else if(strcmp(*field,"TC_2-1-e")==0) {
			 strcpy(cli_py_obj.tc[0].tc_name,"TC_2-1-5");
		}
                if(rval != NULL){
                        cli_py_obj.tc[0].repeat =*((int*)rval);
                        if(Expect && *Expect) {
                           cli_py_obj.Expect_input = (char*) malloc(strlen(*Expect)+1);
                           strcpy(cli_py_obj.Expect_input,*Expect);
                        }else{
                           cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                           strcpy(cli_py_obj.Expect_input,"NILL");
                        }
                }else {
                        cli_py_obj.tc[0].repeat = 0;
                        cli_py_obj.Expect_input = (char*) malloc(sizeof("NILL"));
                        strcpy(cli_py_obj.Expect_input,"NILL");
                }
        }
        perl_command;
        free(cli_py_obj.Expect_input);
	return CPARSER_OK;
}


/**
 * Exit the parser test program.
 */
cparser_result_t
cparser_cmd_quit (cparser_context_t *context)
{
    assert(context);
    return cparser_quit(context->parser);
}


static cparser_result_t
cparser_cmd_enter_privileged_mode (cparser_t *parser, char *buf, int buf_size)
{
    if (strncmp(buf, "HELLO", buf_size)) {
        PRINTF("\nPassword incorrect. Should enter 'HELLO'.\n");
    } else {
        PRINTF("\nEnter privileged mode.\n");
        cparser_set_privileged_mode(parser, 1);
    }
    return CPARSER_OK;
}

cparser_result_t
cparser_cmd_enable_privileged_mode (cparser_context_t *context)
{
    char passwd[100];
    int rc;

    assert(context && context->parser);

    if (cparser_is_in_privileged_mode(context->parser)) {
        PRINTF("Already in privileged mode.\n");
        return CPARSER_NOT_OK;
    }

    /* Request privileged mode password */
    rc = cparser_user_input(context->parser, "Enter password (Enter: 'HELLO'): ", 0,
                            passwd, sizeof(passwd), cparser_cmd_enter_privileged_mode);
    assert(CPARSER_OK == rc);
    return CPARSER_OK;
}

cparser_result_t
cparser_cmd_disable_privileged_mode (cparser_context_t *context)
{
    assert(context && context->parser);
    if (!cparser_is_in_privileged_mode(context->parser)) {
        PRINTF("Not in privileged mode.\n");
        return CPARSER_NOT_OK;
    }

    cparser_set_privileged_mode(context->parser, 0);
    return CPARSER_OK;
}

