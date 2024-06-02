#!/usr/bin/env python 

import pyparsing as pp


file = "test/81-2-10.pat"

f = open(file, "r")
data = open(file, "r")
data = f.read()

### grammar

patt_def = pp.Literal("SNNS pattern definition file V3.2")                                               
generated = pp.Literal("generated at")
num_pat = pp.Literal("No. of patterns :") 
num_inputs = pp.Literal("No. of input units :")                                                          
num_outputs = pp.Literal("No. of output units :")                                                          
INT = pp.Word(pp.nums).set_parse_action(lambda s, l, t: [int(t[0])])
FLOAT = pp.Combine(pp.Optional("-") + pp.Optional(pp.Word(pp.nums)) + "." + pp.Word(pp.nums)
).setParseAction(lambda s, l, t: [float(t[0])])


COMMETS = pp.Literal('# Input pattern no. :') + INT
COMMENT_OUT = pp.Literal('# Output pattern no. :') +  INT                                                        
NUM_INPUTS = num_inputs.suppress() + INT("num_input")
NUM_PAT = num_pat + INT("num_patt")  
NUM_OUTS = num_outputs + INT("num_output")

header = patt_def + generated + NUM_PAT +  \
     NUM_INPUTS + NUM_OUTS 

body = COMMETS  + 81 * FLOAT + COMMENT_OUT +  2 * FLOAT
### end of grammar
parser = header + body 


result = parser.parse_string(data)
print(result)
print(result.dump())

"""
SNNS pattern definition file V3.2                                               
generated at                                                                    
                                                                                
                                                                                
No. of patterns : 45100                                                         
No. of input units : 81                                                         
No. of output units : 2                                                         
                                                                                
# Input pattern no. : 1                                                         
 .00000
 .01016
 .01886
 .02723
 .04098
 .09227
 .10222
 .16545
 .17940
 .23908
 .30128
 .34821
 .39831
 .34066
 .40105
 .56088
 .47320
 .52438
 .50310
 .45034
 .48724
 .35858
 .52162
 .46570
 .48767
 .46701
 .40921
 .43528
 .53704
 .40362
 .40979
 .40361
 .38252
 .33416
 .43406
 .42204
 .35092
 .44773
 .43376
 .41167
 .40276
 .33572
 .33349
 .44367
 .37680
 .37411
 .36307
 .41434
 .38010
 .39545
 .33761
 .38531
 .36607
 .34976
 .36889
 .36936
 .35741
 .31720
 .34022
 .33997
 .34594
 .37011
 .30302
 .35063
 .34486
 .34457
 .34859
 .34571
 .37903
 .30466
 .33606
 .35124
 .29295
 .31243
 .31840
 .29911
 .30506
 .26976
 .32182
 .24593
 .33183
# Output pattern no. : 1                                                        
 .50000   .50000
# Input pattern no. : 2                                                         
 .00000
 .01072
 .01760
 .02937
 .04533
 .07170
 .10681
 .15855
 .23578
 .27401
 .35773
 .32609
 .33867
 .34003
 .38844
 .47920
 .44142
 .47019
 .48123
 .48688
 .50662
 .46880
 .45176
 .45214
 .53081
 .41750
 .40480
 .44266
 .41914
 .42034
 .32657
 .42642
 .40943
 .48295
 .40061
 .49344
 .37910
 .41252
 .37859
 .37769
 .30819
 .45327
 .38256
 .42158
 .39110
 .36935
 .35041
 .45588
 .37106
 .37849
 .35077
 .40028
 .36117
 .35010
 .33781
 .37909
 .40996
 .42064
 .38076
 .29938
 .38070
 .31666
 .36761
 .27903
 .38425
 .31596
 .38811
 .35819
 .38637
 .37561
 .34524
 .28797
 .22642
 .35083
 .32830
 .28515
 .30179
 .32597
 .28126
 .32773
 .29785
# Output pattern no. : 2                                                        
 .50000   .50000
# Input pattern no. : 3                                                         
 .00000
 .00985
 .01946
 .03141
 .03944
 .07783
 .12013
 .18590
 .20576
 .23071
 .29795
 .37993
 .51878
 .41587
 .39745
 .52307
 .46694
 .60795
 .50784
 .48918
 .46259
 .54299
 .37446
 """
