#!/usr/bin/env python

import re, sys, glob

print_tree = False
debug = False
end_node = None

#Help description add for TC
def help_add(desc):
    #RPSW START
    if desc == 'TC_1-3-1':
    	return 'memory of the system and its values.';
    elif desc == 'TC_1-3-2':
    	return 'Test for check the System disk.';
    elif desc == 'TC_1-3-3':
    	return 'Check the System hardware in chassis.';
    elif desc == 'TC_1-3-4':
    	return 'Test for check show chassis.';
    elif desc == 'TC_1-3-6':
    	return 'Test for check the USB Disk.';
    elif desc == 'TC_1-1-3':
    	return 'Setting the env variable in ofw prompt.';
    elif desc == 'TC_1-1-4':
    	return 'Test for upgrading the ofw flash.';
    elif desc == 'TC_1-1-5':
    	return 'Test for Update the Flash verifieid.';
    elif desc == 'TC_1-1-8':
    	return 'Test for device list at the OFW prompt.';
    elif desc == 'TC_1-3-5':
    	return 'Killing a process & generate core file.';
    elif desc == 'TC_1-3-7':
    	return 'Test for checking the flash.';
    elif desc == 'TC_1-1-6':
    	return 'Test to Version of the OFW firmware.';
    elif desc == 'TC_1-1-7':
    	return 'Test to write the OFW firmware upgrade.';
    elif desc == 'TC_1-1-9':
    	return 'Test for BIOS update.';
    elif desc == 'TC_1-1-10':
    	return 'Update the bios firmware upgrade.';
    elif desc == 'TC_1-1-11':
    	return 'Querying the Firmware Minikernel Update.';
    elif desc == 'TC_1-1-12':
    	return 'Test the minikernel firmware upgrade.';
    elif desc == 'TC_1-1-13':
    	return 'Update the PROM firmware upgrade.';
    elif desc == 'TC_1-2-2':
    	return 'Linux Version check in the system.';
    elif desc == 'TC_1-2-3':
    	return 'Test for check the Hardware clock.';
    elif desc == 'TC_1-2-4':
    	return 'Test for check Time of the Day.';
    elif desc == 'TC_1-2-5':
    	return 'Test for ping to SSC card.';
    elif desc == 'TC_1-2-6':
    	return 'Test for to check interface detail.';
    elif desc == 'TC_1-2-7':
    	return 'Check interface detail using ethtool.';
    elif desc == 'TC_1-2-8':
    	return 'Test to List loaded modules in chassis.';
    elif desc == 'TC_1-2-9':
    	return 'Test to check interrupt counts in RP.';
    elif desc == 'TC_1-2-a1':
    	return 'Test to Perform the watchdog test in RP.';
    elif desc == 'TC_1-2-a2':
    	return 'Test to collect virtual mem stat in RP.';
    elif desc == 'TC_1-2-1':
    	return 'Not yet implemented';
    #RPSW_END
    #SSC _START
    elif desc == 'TC_2-2-1':
    	return 'Test for Check the EFI version.';
    elif desc == 'TC_2-2-2':
    	return 'Test the set command in efi prompt.';
    elif desc == 'TC_2-2-3':
    	return '8-th Bus numbers on HK,CaveCreek GEs and Niantics (10GE).';
    elif desc == 'TC_2-2-4':
    	return '4-th Bus numbers on HK, CaveCreek GEs and Niantics (10GE)';
    elif desc == 'TC_2-2-5':
    	return 'Check the 7-th Bus on Niantics (10GE).';
    elif desc == 'TC_2-2-5':
    	return 'Check 8-th Bus on Niantics (10GE).';
    elif desc == 'TC_2-2-6':
    	return 'pci 0 1 0 root ports for HD informtaion.';
    elif desc == 'TC_2-2-7':
    	return 'pci 0 3 0 root ports for HK informtaion.';
    elif desc == 'TC_2-2-8':
    	return 'pci 0 2 0 root ports for CaveCreek  informtaion.';
    elif desc == 'TC_2-2-9':
    	return 'pci 80 3 0 root ports for Niantics  informtaion.';
    elif desc == 'TC_2-2-a0':
    	return 'Test for check the HK device access.';
    elif desc == 'TC_2-2-a1':
    	return 'Test for check the NVRAM devices access.';
    elif desc == 'TC_2-2-a2':
    	return 'Not yet implemnted.';
    elif desc == 'TC_2-2-a3':
    	return 'Test for check the CMB communications.';
    elif desc == 'TC_2-2-a4':
    	return 'Test for check the Boot Mode in EFI shell.';
    elif desc == 'TC_2-1-a':
    	return 'Not yet implemented.';
    elif desc == 'TC_2-1-b':
    	return 'Not yet implemented.';
    elif desc == 'TC_2-1-c':
    	return 'Test for check the SSC Bios Version.';
    elif desc == 'TC_2-1-d':
    	return 'Test for check the SSC Board Name.';
    elif desc == 'TC_2-1-e':
    	return 'Test for Check the DCU fpga hardware and firmware version.';
    elif desc == 'TC_2-1-6':
    	return 'Test for  DCU event register.';
    elif desc == 'TC_2-1-7':
    	return 'Test for Get DCU led state.';
    elif desc == 'TC_2-1-8':
    	return 'Test for Ping test of DCU.';
    elif desc == 'TC_2-1-9':
    	return 'Test for  Get EEPROM log entry 0.';
    elif desc == 'TC_2-1-10':
    	return 'Test for  Get EEPROM log status.';
    elif desc == 'TC_2-1-11':
    	return 'Test for Copy dcu golden image into a temp file.';
    elif desc == 'TC_2-1-12':
    	return 'Test for  set debug uart baudrate.';
    elif desc == 'TC_2-1-13':
    	return 'Test for get  main UART baudrate.';
    elif desc == 'TC_2-1-14':
    	return 'Test for set the  main UART baudrate to 115200.';
    elif desc == 'TC_2-1-15':
    	return 'Test for  Get SM debug UART baudrate.';
    elif desc == 'TC_2-1-16':
    	return 'Test for Set SM debug UART baudrate.';
    elif desc == 'TC_2-1-17':
    	return 'Test for Read SM uptime.';
    elif desc == 'TC_2-1-18':
    	return 'Test for Get RTC time from DCU.';
    elif desc == 'TC_2-1-19':
    	return 'Test for Set the Time in DCU via Current.';
    elif desc == 'TC_2-1-20':
    	return 'Test for Get device info (DIB).';
    elif desc == 'TC_2-1-21':
    	return 'Test for Get processor temperature.';
    elif desc == 'TC_2-1-22':
    	return 'Test for  Ping to processor';
    elif desc == 'TC_2-1-23':
    	return 'Test for Read IA32 MSR.';
    elif desc == 'TC_2-1-24':
    	return 'Test for Read package configuration data.';
    elif desc == 'TC_2-1-25':
    	return 'Test for Read from LPC register.';
    elif desc == 'TC_2-1-26':
    	return 'Test for  Read flash region to file.';
    elif desc == 'TC_2-1-27':
    	return 'Test for DCU  upgrade.';
    elif desc == 'TC_2-1-28':
    	return 'Test for  Flash read.';
    elif desc == 'TC_2-1-29':
    	return 'Test for  Flash Header read.';
    elif desc == 'TC_2-1-30':
    	return 'Test for Flash header write.';
    elif desc == 'TC_2-1-31':
    	return 'Test for  Get the default BIOS image.';
    elif desc == 'TC_2-1-32':
    	return 'Test for  Get IPMI firmware info.';
    elif desc == 'TC_2-1-33':
    	return 'Test for  Get IPMI firmware info.';
    elif desc == 'TC_2-1-34':
    	return 'Test for  Get the IPMI firmware ID.';
    elif desc == 'TC_2-1-35':
    	return 'Test for Get LED status.';
    elif desc == 'TC_2-1-36':
    	return 'Test for Get MAC address info.';
    elif desc == 'TC_2-1-37':
    	return 'Test for get offset from the base address of mac address.';
    elif desc == 'TC_2-1-38':
    	return 'Test for  Get IPMI product ID.';
    elif desc == 'TC_2-1-39':
    	return 'Test for  Get pip protocol version.';
    elif desc == 'TC_2-1-40':
    	return 'Test for Get time from the IPMI.';
    elif desc == 'TC_2-1-41':
    	return 'Test for  PIP interface.';
    elif desc == 'TC_2-1-42':
    	return 'Test for PIP interface - hex.';
    elif desc == 'TC_2-1-43':
    	return 'Test for Get temperature.';
    elif desc == 'TC_2-1-44':
    	return 'Test for LED test.';
    elif desc == 'TC_2-1-45':
    	return 'Test for  Read the BIOS pointer.';
    elif desc == 'TC_2-1-46':
    	return 'Test for Read the default BCS for GEP3.';
    elif desc == 'TC_2-1-47':
    	return 'Test for Read the Return To Factory Default flag.';
    elif desc == 'TC_2-1-48':
    	return 'Test for Read sensor values.';
    elif desc == 'TC_2-1-49':
    	return 'Test for Read sensor table.';
    elif desc == 'TC_2-1-50':
    	return 'Test for check the Default Bios image.';
    elif desc == 'TC_2-1-51':
    	return 'Test for  gfpga.';
    elif desc == 'TC_2-1-52':
    	return 'Test for ssc transmit.';
    elif desc == 'TC_2-1-53':
    	return 'Test for turn off bios debug.';
    elif desc == 'TC_2-1-54':
    	return 'Test for hwclock in SSC.';
    elif desc == 'TC_2-1-55':
    	return 'Test for SSC Time of day.';
    elif desc == 'TC_2-2-15':
    	return 'Test for check the Kernel Version in SSC.';
    elif desc == 'TC_2-2-16':
    	return 'Test for check the HongKong version in SSC.';
    elif desc == 'TC_2-2-17':
    	return 'Test for check the HalfDome  version in SSC.';
    elif desc == 'TC_2-2-18':
    	return 'Test for check the SSC firmware version.';
    elif desc == 'TC_2-2-19':
    	return 'Test for check slot number.';
    elif desc == 'TC_2-3-1':
    	return 'Test for solterm.';
    elif desc == 'TC_2-3-2':
    	return 'Test for check List loaded modules on the system.';
    elif desc == 'TC_2-3-3':
    	return 'Not yet implemented.';
    elif desc == 'TC_2-3-4':
    	return 'Test for check collect virtual mem stat.';
    elif desc == 'TC_2-3-5':
    	return 'Test for check the watchdog test.';
    elif desc == 'TC_2-3-6':
    	return 'Test for to check SSC interface detail.';
    elif desc == 'TC_2-3-7':
    	return 'Test for to check SSC interface information using ethtool.';
    

    return "SSS";


def DBG(hdr, s):
    '''
    Debug printf

    @details Print out an object preceeded by a string header if global "debug" is True.

    @param   hdr A header string.
    @param   s   Data to be displayed.
    '''
    global debug
    if debug:
        sys.stdout.write(hdr)
        print(s)
        
class Node:
    '''A class of parse tree node.'''
    ## Supported token types.
    TOKENS = [ 'ROOT', 'END', 'KEYWORD', 'STRING', 'UINT', 'UINT64', 'INT',
               'INT64', 'HEX', 'HEX64', 'FLOAT', 'MACADDR', 'IPV4ADDR',
               'FILE', 'LIST', 'LINE' ]

    ## Token types and their corresponding C types.
    TYPES = { 'ROOT'       : None,
              'END'        : None,
              'KEYWORD'    : None,
              'STRING'     : 'char *',
              'UINT'       : 'uint32_t ',
              'UINT64'     : 'uint64_t ',
              'INT'        : 'int32_t ',
              'INT64'      : 'int64_t ',
              'HEX'        : 'uint32_t ',
              'HEX64'      : 'uint64_t ',
              'FLOAT'      : 'double ',
              'MACADDR'    : 'cparser_macaddr_t ',
              'IPV4ADDR'   : 'uint32_t ',
              'FILE'       : 'char *',
              'LIST'       : 'char *',
	      'LINE'       : 'char *',
	      'HELP'       : 'char *'
              }
    
    def __init__(self, node_type, param, desc, flags, list_kw=None):
        '''
        Constructor.
        '''

        ## Node type.
        self.type = node_type
        ## Parameter name.
        self.param = param
        ## Node description
        self.desc = ''
        if desc:
          self.desc = '    "%s",\n' % desc
        else :
	  self.desc = '	"NONE",\n';
        ## Flags
        self.flags = flags
	## For Help description.
	if param == 'Number':
	    self.desc = ' "	SSR Number.Count start from 1-N.\\n",\n';
	elif param == 'ipv4':
	    self.desc = ' "IP address[XX:XX:XX:XX] for RPSW1/RPSW2.\\n",\n';
	elif param == 'repeat_value':
	    self.desc = ' "Repeated testcase count.Number starts from 0 to N.\\n",\n';
	elif param == 'slot_number':
	    self.desc = ' "Slot number .Number starts from 1-20.\\n",\n';

        ## List of children nodes
        self.children = []
        if list_kw == None:
            self.list_kw = [] # used only for LIST tokens
        else:
            self.list_kw = list_kw
        
        # Cannot fill these out until we insert the node to the tree
        ## Reference to parent node
        self.parent = None
        ## Depth of the node
        self.depth = 0
        self.path = ''
        self.next = None
        return

    def add_child(self, child):
        '''
        Add a child node to a tree node.

        @param   child A Node object that is added to this node as its child.

        @return  The child node added.
        '''
        for c in self.children:
            if (c.type == child.type) and (c.param == child.param):
                # The node already exists. Re-use the existing node.
                # But check if the hidden flag should be cleared. If the new
                # node does not have CPARSER_NODE_HIDDEN.
                if 'CPARSER_NODE_HIDDEN' not in child.flags:
                    try:
                        c.delete('CPARSER_NODE_HIDDEN')
                    except:
                        pass
                return c
        # Fill out some information that are tree structure dependent.
        # These information are actually embedded in the tree already
        # However, we compute them and cache them to reduce the
        # processing time later. This approach increases the storage
        # requirement but decreases the processing time.
        child.parent = self
        child.depth = self.depth + 1
        if child.is_list():
            # For LIST node, param is a dictionary.
            child.path = self.path + '_' + child.param
        elif child.is_param() or child.is_keyword():
            child.path = self.path + '_' + child.param.replace('-','_')
        elif 'END' == child.type:
            child.path = self.path + '_eol'
        elif 'ROOT' == child.type:
            # If we are adding a child ROOT node, the parent ('self' here)
            # must be an END node. For END node, we insert a string
            # 'cparser_glue' to the front of self.path. So, we must
            # remove it first before creating the submode root path
            child.path = self.param.replace('cparser_glue', '') + '_root'
        if len(self.children) > 0:
            self.children[-1].next = child
        
        # Insert the node into the children list
        self.children.append(child)
        return child

    def is_param(self):
        '''Is this node a parameter node.

        @return  True if it is a parameter node; False it is a keyword node.
        '''
        if (('ROOT' == self.type) or ('END' == self.type) or ('KEYWORD' == self.type)):
            return False
        return True

    def is_keyword(self):
        '''
        Is this node a keyword node.

        @return  True if it is a keyword node; False it is a parameter node.
        '''
        return ('KEYWORD' == self.type)

    def is_list(self):
        '''
        Is this node a LIST node.

        @return  True if it is a LIST node; False otherwise.
        '''
        return ('LIST' == self.type)

    def is_optional(self):
        '''
        Is this node an optional keyword / parameter.

        @return  True if it is optional; False otherwise.
        '''
        return (0 < (self.flags.count('CPARSER_NODE_FLAGS_OPT_START') +
                     self.flags.count('CPARSER_NODE_FLAGS_OPT_END') +
                     self.flags.count('CPARSER_NODE_FLAGS_OPT_PARTIAL')))

    def __repr__(self):
        '''Representation method.

        @return  A string that describes the Node object.
        '''
        msg = ''
        if 'ROOT' == self.type:
            msg += '<ROOT'
        elif 'KEYWORD' == self.type:
            msg += '<KEYWORD:%s' % self.param
        elif 'END' == self.type:
            msg += '<END'
        elif 'LIST' == self.type:
            msg += '<LIST:%s:%s>' % (','.join(self.list_kw), self.param)
        else:
            msg += '<%s:%s' % (self.type, self.param)
        if len(self.flags) > 0:
            # Create a local copy and strip all CPARSER_NODE_FLAGS_ prefix.
            tmp_list = self.flags[:]
            for n in range(0,len(tmp_list)):
                tmp_list[n] = tmp_list[n].replace('CPARSER_NODE_FLAGS_','')
            msg += str(tmp_list)
        msg += '> '
        return msg

    ## Display a summary of the node.
    def display(self, fout=sys.stdout):
        fout.write(self.__repr__())

    ##
    # \brief     Walk the tree
    #
    # \param     fn     Function to be called per node.
    # \param     mode   'pre-order', 'func', 'post-order'.
    # \param     cookie An opaque object to be passed into 'fn'.
    #
    # \return    Return the number of callback made.
    def walk(self, fn, mode, cookie):
        last = len(self.children)
        count = 0
        if (mode == 'pre-order') or (mode == 'func'):
            if ((mode == 'pre-order') or
                ((self.type == 'END') and
                 (not self.flags.count('CPARSER_NODE_FLAGS_OPT_PARTIAL')))):
                fn(self, cookie)
                count += 1
            for n in range(last):
                count += self.children[n].walk(fn, mode, cookie)
        elif 'post-order' == mode:
            for n in range(last):
                count += self.children[last-1-n].walk(fn, mode, cookie)
            fn(self, cookie)
            count += 1
        else:
            raise ValueError, 'Unknown walk mode: %s' % mode
        return count
    
    def c_struct(self):
        '''
        Generate the C structure name.

        @return  Return a string that contains the C structure for the node.
        '''
        msg = ''
        if 'LIST' == self.type:
            # For LIST token, build its nodes. First, build the variable name.
            list_kw_len = len(self.list_kw)
            for n in range(list_kw_len-1, -1, -1):
                this_kw = self.list_kw[n]
                if n == (list_kw_len - 1):
                    next = 'NULL' # last keyword in the list
                else:
                    next = '&cparser_list_node%s_%s' % (self.path, self.list_kw[n+1].replace('-', '_'))
                msg += 'cparser_list_node_t cparser_list_node%s_%s = {\n' % (self.path, this_kw.replace('-', '_'))
                msg += '    %s,\n' % next
                msg += '    "%s",\n' % this_kw
		msg += '    "		%s"\n' % help_add(this_kw)
                msg += ' };\n\n'
            
        if self.parent == None:
            msg += 'cparser_node_t cparser_root = {\n'
        else:
            msg += 'cparser_node_t cparser_node%s = {\n' % self.path
        # type
        msg += '    CPARSER_NODE_%s,\n' % self.type
        # flags
        if len(self.flags) == 0:
            msg += '    0,\n'
        else:
            msg += '    ' + ' | '.join(self.flags) + ',\n'
        # param
        if 'ROOT' == self.type:  msg += '    NULL,\n'
        elif 'END' == self.type: msg += '    %s,\n' % self.param
        elif 'KEYWORD' == self.type: msg += '    "%s",\n' % self.param
        elif 'LIST' == self.type:
            msg += '    &cparser_list_node%s_%s,\n' % (self.path, self.list_kw[0].replace('-', '_'))
        else: msg += '    "<%s:%s>",\n' % (self.type, self.param)
        # desc
        msg += self.desc
        # sibling
        if self.next:
            msg += '    &cparser_node%s,\n' % self.next.path
        else:
            msg += '    NULL,\n'
        # children
        if len(self.children) > 0:
            msg += '    &cparser_node%s\n' % self.children[0].path
        else:
            msg += '    NULL\n'
        msg += '};\n\n'

        return msg

    def walk_up_to_root(self):
        '''
        Return a list of Node objects that forms a path from root to this node.

        @return  A list of Node objects that forms a path from root (first elemnt) to this node (last element).
        '''
        assert self.type == 'END'
        p = []
        cur_node = self
        while cur_node.parent:
            p.insert(0, cur_node)
            cur_node = cur_node.parent
            if cur_node.type == 'ROOT':
                break
        return p

    def action_fn(self):
        '''
        Generate the action function prototype.

        @return  The C action function prototype for a command.
        '''
        # Build a list of parse nodes that forms the path from the root.
        # to this end node
        path = self.walk_up_to_root()

        # Declare the action function
        msg = ('cparser_result_t %s(cparser_context_t *context' %
               self.param.replace('cparser_glue', 'cparser_cmd'))

        # Declare the variable list
        for n in path:
            if not n.is_param(): continue
            msg += ',\n    %s*%s_ptr' % (Node.TYPES[n.type], n.param)
        msg += ');\n'
        return msg

    def glue_fn(self):
        '''
        Generate the glue funtion.
        
        @return  The C glue function for a command.
        '''
        # Build a list of parse nodes that forms the path from the root.
        # to this end node
        path = self.walk_up_to_root()

        # Build the glue function
        msg =  'cparser_result_t\n'
        msg += '%s (cparser_t *parser)\n' % self.param
        msg += '{\n'

        # Declare the variable list
        skip = ''
        for n in path:
            if not n.is_param(): continue
            skip = '\n'
            val_type = Node.TYPES[n.type]
            msg += '    %s%s_val;\n' % (val_type, n.param)
            msg += '    %s*%s_ptr = NULL;\n' % (val_type, n.param)
        if skip: msg += '    cparser_result_t rc;\n'
        msg += skip
        
        # Extract the parameters
        k = -1
        for n in path:
            k = k + 1
            if not n.is_param(): continue
            msg += ('    rc = cparser_get_%s(&parser->tokens[%d], &%s_val);\n' %
                    (n.type.lower(), k, n.param))
            if n.is_optional():
                msg += '    if (CPARSER_OK == rc) {\n'
                msg += '        %s_ptr = &%s_val;\n' % (n.param, n.param)
                msg += '    } else {\n'
                msg += '        assert(%d > parser->token_tos);\n' % (k+1)
                msg += '    }\n'
            else:
                msg += '    assert(CPARSER_OK == rc);\n'
                msg += '    %s_ptr = &%s_val;\n' % (n.param, n.param)

        # Call the user-provided action function
        msg += ('    %s(&parser->context' %
                self.param.replace('cparser_glue', 'cparser_cmd'))
        for n in path:
            if n.is_param(): msg += ',\n        %s_ptr' % n.param
        msg += ');\n'
        msg += '    return CPARSER_OK;\n'
        msg += '}\n\n'
        return msg

class Token:
    '''Token class. This class represents a token in a CLI command.'''
    ## Beginning of a parameter token
    BEGIN = '^\<'
    ## End of a parameter token
    END = '\>$'
    ## Token type
    TYPE = '([A-Z][A-Z0-9]*)'
    ## Keyword
    KW = '[a-zA-Z0-9_-]+'
    LIST_KW = '([^:]+)'
    ## Parameter name
    PARAM = '([a-zA-Z][a-zA-Z0-9_+]*)'
    ## Description of a node
    DESC= '(:(.+))*'
    
    @classmethod
    def valid_keyword(cls, s):
        '''Check whether a string is a valid keyword.
        
        @return  True if the string is a valid keyword; False otherwise.
        '''
        return bool(re.search('^' + cls.KW + '$', s))
        
    def __init__(self, s):
        '''Constructor.
        
        @param   s Token string.
        '''

        # Create the fields of this object
        ## Node type
        self.type = ''
        ## Parameter name
        self.param = ''
        ## Description of the node
        self.desc = ''
        ## If it is a LIST node, list of keywords.
        self.list_kw = []
        
        # Check if this is a keyword
        if Token.valid_keyword(s):
            self.type = 'KEYWORD'
            self.param = s
	    self.desc = 'NODE\\n'
	    if s == 'rpsw1':
	    	self.desc = '		RPSW1 related testcase.\\n';
	    elif s == 'rpsw2':
	   	self.desc = '		RPSW2 related testcase.\\n';
	    elif s == 'ssr':
	    	self.desc = '		Complete SSR related testcase.\\n';
	    elif s == 'enable':
	    	self.desc = '		Enable to super user root{Don\'t use now}.\\n';
	    elif s == 'quit' :
	    	self.desc = '		Exit from SSR_UT Automation.\\n';
	    elif s == 'ssc1' :
	    	self.desc = '		SSC1 type card related testcase.\\n';
	    elif s == 'ssc2-a':
	    	self.desc = '		SSC2-a type card related testcase.\\n';
	    elif s == 'ssc1-v2':
	    	self.desc = '	SSC1-v2 type card related testcase.\\n';
	    elif s == 'console-ip':
	    	self.desc = '	Console ip address of RPSW1/RPSW2.\\n';
	    elif s == 'slot':
		self.desc = '		Slot number in chassis for SSC card.\\n';
	    elif s == 'ipos':
	    	self.desc = '		IPOS Prompt Related testcase.\\n';
	    elif s == 'shell':
	    	self.desc = '		Shell Prompt Related testcase.\\n';
	    elif s == 'efi':
	    	self.desc = '		EFI Prompt Related testcase.\\n';
	    elif s == 'ofw':
	    	self.desc = '		OFW Prompt Related testcase.\\n';
	    elif s == 'Repeat':
	    	self.desc ='		Repeat the testcase.\\n';
            self.list_kw = []
            return None
        
        # This token must be a parameter of some kind. Parse the type.
        m = re.search(Token.BEGIN + Token.TYPE + ':(.+)' + Token.END,  s)
        if not m:
            raise ValueError, 'Invalid token "%s".' % s
        if m.group(1) not in Node.TYPES:
            raise ValueError, 'Unknown token type "%s".' % m.group(1)
        self.type = m.group(1)
        
        # Check if it is a LIST type.
        if self.type == 'LIST':
	
            m = re.search(Token.BEGIN + Token.TYPE + ':' + Token.LIST_KW + ':' + 
                          Token.PARAM + Token.DESC + Token.END, s)
            if not m:
                raise ValueError,  'Malformed LIST token "%s".' % s
            (self.type,  list_kw,  self.param, dummy, self.desc) = m.groups()
            # Validate all keywords in the list
            self.list_kw = list_kw.split(',')
            for kw in self.list_kw:
                if not self.valid_keyword(kw):
                    raise ValueError,  'Invalid LIST keyword "%s".' % kw
            return None
        
        # Handle the rest of the parameters
        m = re.search(Token.BEGIN + Token.TYPE + ':' + Token.PARAM + Token.DESC + Token.END,  s)
        if not m:
            m = re.search(Token.BEGIN + Token.TYPE + ':([^:>]+)' + Token.DESC + Token.END,  s)
            assert m
            raise ValueError, 'Invalid parameter name "%s".' % m.group(2)
        (self.type, self.param, dummy, self.desc) = m.groups()
        self.list_kw = []

##
# \brief     Add one line of CLI to the parse tree.
#
# \param     root     Root node of the parse tree.
# \param     line     A line of command from a CLI file.
# \param     comment  The comment that goes with this line of command.
#
# \return    Return a new root node.
def add_cli(root, line, comment):
    global end_node
    nodes = []
    flags = []
    hidden_flag = []
    num_opt_start = 0
    num_opt_end = 0

    # Convert a line into a token list
    line = line.replace('\n','')
    DBG('\n  LINE: ', line)
    tokens = line.split(' ')

    # Delete all token that is ''
    cnt = tokens.count('')
    for k in range(0, cnt):
        tokens.remove('')
    if len(tokens) == 0:
        return root # this is a blank line. quit

    # If the '+' marker is with the first token, separate them
    if tokens[0] == '+':
        tokens.pop(0)
        hidden_flag = [ 'CPARSER_NODE_FLAGS_HIDDEN', ]
    elif tokens[0][0] == '+':
        tokens[0] = tokens[0][1:]
        hidden_flag = [ 'CPARSER_NODE_FLAGS_HIDDEN', ]

    # Convert tokens to parse tree nodes. '{' and '}' do not produce tree
    # nodes. But they do affect the flags used in some nodes.
    start_flag = False
    for t in tokens:
        # Parse each token
        # Look for '{'
        if '{' == t:
            # In the last node, its flags field is a reference to
            # 'flags'. So, if we append to it, the last node will get
            # a new flag.
            start_flag = True
            num_opt_start = num_opt_start + 1
            continue 
        # Look for '}'
        if '}' == t:
            # See comment in '{' case.
            assert(len(nodes) > 0)
            nodes[-1].flags.append('CPARSER_NODE_FLAGS_OPT_END')
            num_opt_end = num_opt_end + 1
            if num_opt_end == num_opt_start:
                nodes[-1].flags.remove('CPARSER_NODE_FLAGS_OPT_PARTIAL')
            continue

        if num_opt_start > num_opt_end:
            flags = hidden_flag + ['CPARSER_NODE_FLAGS_OPT_PARTIAL',]
        else:
            flags = hidden_flag[:]

        if start_flag:
            flags.append('CPARSER_NODE_FLAGS_OPT_START')

        # Get the token type
        tt = Token(t)
        nodes.append(Node(tt.type, tt.param, tt.desc, flags[:], tt.list_kw))
        start_flag = False

    # hack alert - Check that if there are optional parameters, the format is ok
    
    DBG('TOKENS: ', tokens)
    if debug:
        sys.stdout.write(' NODES: ')
        for nn in nodes[:-1]:
            nn.display()
            sys.stdout.write('\n        ')
        nodes[-1].display()
        sys.stdout.write('\n')

    # We need to create the glue function name. Since the path of the node
    # is set up when the node is inserted, we don't have it here. So,
    # we manually walk all the nodes and generate the glue function name
    glue_fn = 'cparser_glue' + root.param
    for n in nodes:
        glue_fn = glue_fn + '_' + n.param.replace('-','_')
    
    # Insert them into the parse tree
    for k in range(0, num_opt_start+1):
        DBG('   CLI: ', k)
        num_braces = 0
        cur_node = root
        if num_opt_start == k:
            end_node = Node('END', glue_fn, comment, hidden_flag[:])
        else:
            end_node = Node('END', glue_fn, None, ['CPARSER_NODE_FLAGS_OPT_PARTIAL',] + hidden_flag)
        for n in nodes:
            if n.flags.count('CPARSER_NODE_FLAGS_OPT_START'):
                if num_braces == k:
                    num_braces += 1
                    break
                num_braces += 1
            if debug:
                sys.stdout.write('        ')
                cur_node.display()
                sys.stdout.write('-> ')
                n.display()
                sys.stdout.write('\n')
            cur_node = cur_node.add_child(n)
        if debug:
            sys.stdout.write('        ')
            cur_node.display()
            sys.stdout.write('-> ')
            end_node.display()
            sys.stdout.write('\n')
        cur_node.add_child(end_node)
    return root

##
# \brief     Process one .cli file. This includes handling all
#            preprocessors directive.
#
def process_cli_file(filename, root, mode, labels, last_cli_root=None, last_cli_end=None, submode=False):
    '''
    Process one .cli file. This includes handling all preprocessors directive.

    @param     filename Name of the .cli file.
    @param     root     Root Node object of the parse tree.
    @param     mode     "compile", "preprocess" or "mkdep"
    @param     labels   A dictionary containing all defined labels used in
                        preprocessing.
    @param     last_cli_root The most recent root node created.
    @param     last_cli_end  The most recent end node visited.
    @param     submode  A boolean of whether we are in a submode.

    @return    Return the new root node.
    '''
    
    num_disable = 0
    label_stack = []
    deplist = []
    comment = None
    line = ''
    try:
        fin = open(filename, 'r')
    except:
        print 'Fail to open %s.' % filename
        sys.exit(-1)
        
    line_num = 0
    for line in fin:
        line_num = line_num + 1

        # Process the file line by line. The orderof processing
        # These different directives is extremely important. And the
        # order below is not arbitrary.
        #
        # We must process #endif not matter what. Otherwise, once
        # we start a #ifdef block that is omitted, we'll never be able
        # to terminate it. Then, we omit every other type of line as long
        # as there is at least one disable #ifdef left. Afterward, we
        # check for illegal directives. A normal command line is handled
        # last. Illegal tokens are checked inside add_cli().

        # #endif
        m = re.search('^#endif', line)
        if m:
            if len(label_stack) == 0:
                print('%s:%d: Unmatched #ifdef/#ifndef' % (filename, line_num))
                sys.exit(-1)
            num_disable = num_disable - label_stack.pop(0)[1]
            continue
        # Skip the rest of processing because some #ifdef/#ifndef is
        # keeping this line from being processed.
        if (num_disable > 0):
            continue
        # Check for illegal preprocessor directives
        if (re.search('^#', line) and
            (not re.search('^#ifdef(\S*\/\/.*)*', line) and
             not re.search('^#submode(\S*\/\/.*)*', line) and
             not re.search('^#endsubmode(\S*\/\/.*)*', line) and
             not re.search('^#include(\S*\/\/.*)*', line))):
            print('%s:%d: Unknown preprocessor directive.' % (filename, line_num))
            sys.exit(-1)
        # Comment
        m = re.search('^\s*\/\/\s*(.*)', line)
        if m:
            if 'compile' == mode:
                comment = m.group(1)
            if 'preprocess' == mode:
                sys.stdout.write(line)
            continue
        # #ifdef
        m = re.search('^#ifdef (.+)', line)
        if m:
            l = m.group(1)
            val = 0
            if not labels.has_key(l):
                val = 1
                num_disable = num_disable + 1
            label_stack.insert(0, [l, val])
            continue
        # #ifndef
        m = re.search('^#ifndef (.+)', line)
        if m:
            l = m.group(1)
            val = 0
            if labels.has_key(m.group(1)):
                val = 1
                num_disable = num_disable + 1
            label_stack.insert(0, [l, val])
            continue
        # #include
        m = re.search('^#include "(.+)"', line)
        if m:
            if len(glob.glob(m.group(1))) == 0:
                print('%s:%d: file %s does not exist.' %
                      (filename, line_num, m.group(1)))
                sys.exit(-1)
            if ('compile' == mode):
                process_cli_file(m.group(1), root, mode, labels, last_cli_root, last_cli_end, submode)
            elif ('mkdep' == mode):
                deplist.append(m.group(1))
            elif ('preprocess' == mode):
                process_cli_file(m.group(1), root, mode, labels, last_cli_root, last_cli_end, submode)
            else:
                print('%s:%d: unknown mode %s' % (filename, line_num, mode))
            continue
        # #submode
        m = re.search('^#submode "(.+)"', line)
        if m:
            if submode:
                print('%s:%d: nested submode is invalid.' % (filename, line_num))
            else:
                submode = True
                last_cli_root = Node('ROOT', '_' + m.group(1),
                                     'Root of submode %s' % m.group(1), [])
                last_cli_end.add_child(last_cli_root)
            continue
        # #endsubmode
        m = re.search('^#endsubmode', line)
        if m:
            if not submode:
                print('%s:%d: #endsubmode without a #submode.' %
                      (filename, line_num))
                sys.exit(-1)
            else:
                submode = False
                last_cli_root = None
                last_cli_end = None
            continue
        # What survive must be either an empty line or a command
        if ('compile' == mode):
            try:
                if not submode:
                    root = add_cli(root, line, comment)
                    last_cli_end = end_node
                else:
                    last_cli_root = add_cli(last_cli_root, line, comment)
            except ValueError, msg:
                print('%s:%d: %s' % (filename, line_num, msg))
                sys.exit(-1)
        elif ('preprocess' == mode):
            sys.stdout.write(line)
        comment = None
    if 'mkdep' == mode:
        sys.stdout.write('%s:' % filename)
        for d in deplist: sys.stdout.write(' %s' % d)
        sys.stdout.write('\n')
    return root

def walker_gen_dbg(node, fout):
    '''
    Display each node.

    @param       node A Node object.
    @param       fout An output file object.
    '''
    fout.write('  ' * node.depth)
    node.display()
    fout.write('\n')

def main():
    '''Program entry point.'''
    filelist = []
    labels = {}
    mode = 'compile'
    out_dir = '.'
    c_fname = 'cparser_tree.c'
    h_fname = 'cparser_tree.h'
    # Parse input arguments
    sys.argv.pop(0) # remove mk_parser.py itself
    while (len(sys.argv) > 0):
        item = sys.argv.pop(0)
        if '-MM' == item:
            mode = 'mkdep'
        elif '-P' == item:
            mode = 'preprocess'
        elif '-D' == item:
            l = sys.argv.pop(0)
            labels[l] = 0;
        elif '-o' == item:
            out_dir = sys.argv.pop(0)
        elif '-c' == item:
            c_fname = sys.argv.pop(0)
        elif '-i' == item:
            h_fname = sys.argv.pop(0)
        else:
            filelist.append(item)

    # Process each file
    root = Node('ROOT', '', 'Root node of the parser tree', [])
    for f in filelist:
        if ('mkdep' != mode):
            print('Processing %s...' % f)
        root = process_cli_file(f, root, mode, labels)
    if print_tree:
        root.walk(walker_gen_dbg, 'pre-order', sys.stdout)

    # Generate .c file that contains glue functions and parse tree
    c_fname = out_dir + '/' + c_fname
    try:
        fout = open(c_fname, 'w')
    except:
        print 'Fail to open %s.' % c_fname
        sys.exit(-1)
    fout.write('/*----------------------------------------------------------------------\n' +
               ' * This file is generated by mk_parser.py.\n' + 
               ' *----------------------------------------------------------------------*/\n' +
               '#include <assert.h>\n' +
               '#include <stdint.h>\n' +
               '#include <stdio.h>\n' +
               '#include "cparser.h"\n' +
               '#include "cparser_priv.h"\n' +
               '#include "cparser_token.h"\n' +
               '#include "cparser_tree.h"\n\n')    
    n_cmds = root.walk(lambda n,f: f.write(n.glue_fn()), 'func', fout)
    n_nodes = root.walk(lambda n,f: f.write(n.c_struct()), 'post-order', fout)
    fout.close()

    h_fname = out_dir + '/' + h_fname
    try:
        fout = open(h_fname, 'w')
    except:
        print 'Fail to open %s.' % h_fname
        sys.exit(-1)
    fout.write('/*----------------------------------------------------------------------\n' +
               ' * This file is generated by mk_parser.py.\n' +
               ' *----------------------------------------------------------------------*/\n' +
               '#ifndef __CPARSER_TREE_H__\n' +
               '#define __CPARSER_TREE_H__\n\n' +
               '#ifdef __cplusplus\n' +
               'extern "C" {\n' +
               '#endif /* __cplusplus */\n\n' +
               'extern cparser_node_t cparser_root;\n\n')
    root.walk(lambda n,f: f.write(n.action_fn()), 'func', fout)
    fout.write('\n#ifdef __cplusplus\n' +
               '}\n' +
               '#endif /* __cplusplus */\n' +
               '\n#endif /* __CPARSER_TREE_H__ */\n')
    fout.close()

    # Print out a summary
    print '%d commands.' % n_cmds
    print '%d parse tree nodes (%d bytes).' % (n_nodes, n_nodes * 24)

    return

# Entry point of the script
if __name__ == '__main__':
    main()

