/**
 * \file     cparser_options.h
 * \brief    Parser limits for various objects.
 */

#ifndef __CPARSER_OPTIONS_H__
#define __CPARSER_OPTIONS_H__

/**
 * Maximum number of character of a command prompt including the 
 * terminating NULL.
 */
#define CPARSER_MAX_PROMPT         (100)

/**
 * Maximum number of nested sub-mode levels.
 */
#define CPARSER_MAX_NESTED_LEVELS  (200)

/**
 * Maximum number of characters in one token.
 */
#define CPARSER_MAX_TOKEN_SIZE     (256)

/**
 * Maximum number of token per line.
 */
#define CPARSER_MAX_NUM_TOKENS     (3200)

/**
 * Maximum number of lines.
 */
#define CPARSER_MAX_LINES          (100)

/**
 * Maximum number of character per line.
 */
#define CPARSER_MAX_LINE_SIZE      (3830)

/**
 * If defined, support some of Emacs key binding.
 */
#define CPARSER_EMACS_BINDING

#endif /* __CPARSER_OPTIONS_H__ */
