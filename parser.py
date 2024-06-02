#!/usr/bin/env python 

import pyparsing as pp

from pyparsing import (
    Group,
)

file = "test/10-2-5.pat"

x_num_patt = 10
x_num_input = 5
x_num_output = 2
f = open(file, "r")
data = open(file, "r")
data = f.read()

### grammar
def grammar():

    patt_def = pp.Literal("SNNS pattern definition file V3.2").suppress()
    generated = pp.Literal("generated at").suppress()
    num_pat = pp.Literal("No. of patterns :") 
    num_inputs = pp.Literal("No. of input units :")                                                          
    num_outputs = pp.Literal("No. of output units :")                                                          
    INT = pp.Word(pp.nums).set_parse_action(lambda s, l, t: [int(t[0])])
    FLOAT = pp.Combine(pp.Optional("-") + pp.Optional(pp.Word(pp.nums)) + "." + pp.Word(pp.nums)
    ).setParseAction(lambda s, l, t: [float(t[0])])


    COMMETS = pp.Literal('# Input pattern no. :') + INT
    COMMENT_OUT = pp.Literal('# Output pattern no. :') +  INT                                                        
    NUM_INPUTS = num_inputs.suppress() + INT("num_input")
    NUM_PAT = num_pat.suppress() + INT("num_patt")  
    NUM_OUTS = num_outputs.suppress() + INT("num_output")

    header = Group(patt_def + generated + NUM_PAT +  NUM_INPUTS + NUM_OUTS )

    one_pattern = Group( Group(COMMETS.suppress()  + x_num_input * FLOAT) + \
            Group(COMMENT_OUT.suppress() +  x_num_output * FLOAT))
    body = Group( x_num_patt* one_pattern )
    ### end of grammar
    parser = header + body 

    return parser


def build_dictionary( d):

    parser = grammar()
    result = parser.parse_string(d)
    print(result.dump())


build_dictionary(data)
