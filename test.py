from interpreterv3 import Interpreter

object_assignment = [
'func main void  ',
'  var object x',
'  assign x.a 10 				# x.a’s type is int',
'  var int y',
'  assign y 20',
'',
'  assign y * x.a y',
'  funccall print y			# prints 200',
'endfunc'
]

fail_26 = [
'func main void',
'  var object x',
'  funccall print x.a',
'endfunc']

fail_105 = [
'func main void',
'  var object o',
'  assign o.a 100',
'  if True',
'    assign o.a "bar"',
'    var object o',
'    assign o.b True',
'    if == o.b False',
'      funccall print o.a',
'    else',
'      assign o.a 10',
'    endif',
'    var int y',
'    assign y - o.a 8',
'  endif',
'  var int z',
'  assign z + o.a 5',
'  funccall print z',
'endfunc']

func_var_call = [
'func inc x:int int',
'  return + x 1',
'endfunc',
'',
'func main void',
' var func f			# f has a type of func and is a func variable',
' assign f inc           # f holds the inc function!',
' funccall f 10          # call inc thru f',
' funccall print resulti # prints 11',
'endfunc',
]

func_pass = [
'func takes_a_function f:func void',
'  funccall f 10',
'endfunc',
'',
'func foo x:int void',
'  funccall print x',
'endfunc',
'',
'func main void',
'  funccall takes_a_function foo',
'endfunc']

return_func = [
'func foo x:int int',
'  return + x 1',
'endfunc',
'',
'func bar func',
'  return foo',
'endfunc',
'',
'func main void',
'  var func f',
'',
'  funccall bar',
'  assign f resultf        # resultf contains foo',
'  funccall f 10',
'  funccall print resulti  # prints 11',
'endfunc']

pass_by_obj_ref = [
'func main void',
'  var object x',
'  assign x.member1 42',
'  assign x.member2 "blah"',	 
'  funccall foo x',
'  funccall print x.member2',
'endfunc',
'',
'func foo q:object void',
'  funccall print q.member1',
'  assign q.member2 "bletch"  # mutates original x.member2 variable',
'endfunc']

return_obj = [
'func bar object   # the bar function returns an object',
'  var object x',
'  assign x.a 10',
'  assign x.b True',
'  return x',
'endfunc',
'',
'func main void',
'  var object q',
'',
'  funccall bar',
'  assign q resulto        # resulto contains x',
'  funccall print q.b      # prints True',
'endfunc']

dot_notation = [
'func main void',
'  var object x',
'  assign x.a 10',
'  assign x.b "salamander"',
'  funccall print x.a x.b',
'endfunc']

linked_list = [
'func main void',
'  var object x y z',
'  assign x.a 10',
'',
'  assign y.my_member x',
'  assign z y.my_member',
'',
'  funccall print z.a   # prints 10',
'endfunc'
]

member_func = [
'func f i:int void',
'  assign i + 100 i',
'  funccall print i',
'endfunc',
'',
'func main void',
'  var object x',
'',
'  assign x.some_method f  		# x.some_method points at f()',
'  funccall x.some_method 52		# calls f(52)',
'',
'  var func my_func',
'  assign my_func f			# my_func holds f',
'',
'  assign x.second_method my_func    # x.second_method points at f()',
'  funccall x.second_method 13',
'endfunc'
]

type_error = [
'func main void  ',
'  var string xyz',
'  assign xyz.a 10  	# results in a type error when this line runs',
'endfunc']

shallow_copy = [
'func main void',
'  var object o p',
'',
'  assign o.x 10',
'  assign p o		# p now refers to the same object that o does.',
'  assign p.x 20',
'  funccall print o.x  	# prints 20',
'endfunc'
]

this_test = [
'func f i:int void',
'  assign this.val i    # this refers to the x variable, below',
'endfunc',
'',
'func main void',
'  var object xyz',
'',
'  assign xyz.val 42',
'  assign xyz.method f',
'',
'  funccall xyz.method 52',
'  funccall print xyz.val  	# prints 52',
'endfunc'
]

undef_this = [
'func f i:int void',
'  assign this.val i    # Name error! “this” is undefined!',
'endfunc',
'',
'func main void',
'  var object x',
'',
'  assign x.val 42',
'  assign x.method f',
'',
'  funccall f 52',
'  funccall print x.val  	# never gets here',
'endfunc'
]

nonfunc_mem_var = [
'func main void',
'  var object x',
'',
'  assign x.val 42',
'  funccall x.val 52		# x.val is an integer, not a func',
'endfunc']

undef_mem_var = [
'func main void',
'  var object x',
'',
'  assign x.val 42',
'  funccall x.blah 52		# name error; x.blah doesn’t exist',
'endfunc']

lambda_test_1 = [
'func main void',
' var int capture_me',
' assign capture_me 42',
'',
' lambda a:int int                 # defines a lambda for int f(int)',
'  return + a capture_me		   # captures the capture_me variable',
' endlambda',
' # resultf holds the closure created by the lambda',
'',
' var func f',
' assign f resultf			# f now points to the closure',
' funccall f 10			# calls our lambda function!',
' funccall print resulti    	# prints 52',
'endfunc']

lambda_test_2 = [
'func main void',
' var int capture_me		# captured',
' assign capture_me 42',
'',
' if > capture_me 10',
'   var int capture_me_too	# also captured',
'   assign capture_me_too 1000',
'   lambda a:int int',
'    return + + a capture_me capture_me_too',
'   endlambda',
' endif',
'',
' funccall resultf 10		# resultf contains our closure',
' funccall print resulti		# prints 1052',
'endfunc']

lambda_copy = [
'func main void',
'  var int a',
'  var object o',
'',
'  assign a 5',
'  assign o.x 10',
'',
'  lambda void',
'    assign a + a 1',
'    funccall print a        # prints 6',
'    assign o.x 20',
'    funccall print o.x      # prints 20',
'  endlambda',
'',
'  var func f',
'  assign f resultf',
'  funccall f',
'',
'  funccall print a          # prints 5',
'  funccall print o.x        # prints 10',
'endfunc'
]

lambda_nesting = [
'func main void',
'  var int capture_me',
'  assign capture_me 1000',
'  lambda a:int func			# outer lambda',
'   var int capture_me2',
'   assign capture_me2 10000',
'   lambda b:int int			# nested lambda',
'    return + + + a capture_me b capture_me2',
'   endlambda',
'   return resultf',
'  endlambda',
'',
' var func f g',
' assign f resultf		# f points at the outer lambda/closure',
' funccall f 10',
' assign g resultf		# g points at the inner lambda',
' funccall g 42',
' funccall print resulti		# prints 11052',
'endfunc'
]

lambda_shadowing = [
'func main void',
' var int capture_me',
' assign capture_me 42',
'',
' if > capture_me 10',
'   var int capture_me',
'   assign capture_me 1000',
'   lambda a:int int',
'    return + a capture_me	# the captured capture_me’s value is 1000',
'   endlambda',
' endif',
'',
' var func f',
' assign f resultf',
' funccall f 10',
' funccall print resulti		# prints 1010',
'endfunc'
]

create_lambda = [
'# this is in the spec!',
'',
'func create_lambda x:int func',
'  lambda y:int int     # defines a lambda/closure and stores in resultf',
'    var int z',
'    assign z + x y',
'    return z',
'  endlambda',
'',
'  return resultf       # return our lambda/closure',
'endfunc',
'',
'func main void',
'  var func f g',
'  funccall create_lambda 10   # create a lambda that captures x=10',
'  assign f resultf            # f holds our lambdas closure',
'',
'  funccall create_lambda 100  # create a lambda that captures x=100',
'  assign g resultf            # f holds our lambdas closure',
'',
'  funccall f 42',
'  funccall print resulti      # prints 52',
'',
'  funccall g 42',
'  funccall print resulti      # prints 142',
'endfunc']


i = Interpreter(console_output=True, trace_output=True)
i.run(create_lambda)

# [x:(t:Object, v:{})]

# test default func working 
