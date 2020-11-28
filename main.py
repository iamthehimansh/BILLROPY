from flask import Flask , render_template,request,redirect,send_from_directory,make_response,render_template_string
from waitress import serve
import pdfkit
import random
import json
from datetime import date
import Checksum 
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
roboapp=Flask(__name__)

roboapp.config['SECRET_KEY']="iamthehimanshGOd"
# person_not_avilabe_count=0
# person_avilable_frist_time=False
from runit import auto_pilot_for_billropy
import open_cv_object_deaction as obj_deaction
# print(main.get_object_name(1))
class presonavility:
    def __init__(self):
        self.person_avilable_frist_time=True
    def get(self):
        return self.person_avilable_frist_time
    def set(self,value):
        self.person_avilable_frist_time=value

person_frist_time=presonavility()


class person_not_avilable:
    """Person not avilable count"""
    def __init__(self):
        self.person_not_avilabe_count=0
    def increase(self):
        self.person_not_avilabe_count+=1
    def zero(self):
        self.person_not_avilabe_count=0
    def get(self):
        return self.person_not_avilabe_count
    
count1=person_not_avilable()

class stoped:
    """docstring for stoped"""
    def __init__(self):
        self.stoped=False
    def get(self):
        return self.stoped
    def set(self,value):
        self.stoped=value

mystoped_obj=stoped()

        
        



def callPersonAvilityCheacker():
    z=obj_deaction.get_object_name()
    main_data={}
    for i in z:
        if i.lower()=="person":
            main_data["person_avilable"]=True
    try:
        d=main_data["person_avilable"]
    except:
        main_data["person_avilable"]=False
    return main_data

    
# this funcution call tencorfow and get data about person ability

# global variables
MERCHANT_KEY="vf%nzR5jz2JU5WM_"
chromedriver = r"C:\Users\IamTheHimansh\Documents\BILLROPY\static\chromedriver.exe"
continuetomessagexpath=r'//*[@id="action-button"]'
messagexpath=r'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
sendbtnxpath=r'//*[@id="main"]/footer/div[1]/div[3]'
driver = webdriver.Chrome(chromedriver)

# calling function 1st time when server get started
def callwhtappscan():
    try:
        driver.get("https://web.whatsapp.com/")
    except:
        try:
            driver.get("https://web.whatsapp.com/")
        except:
            try:
                driver.get("https://web.whatsapp.com/")
            except:
                pass


@roboapp.route("/")
@roboapp.route("/home")
@roboapp.route("/index")
def home():
    with open("data.json","r")as rf:
        data=json.load(rf)
    with open ("offer.json","r") as rf2:
        jd=json.load(rf2)
    if jd["status"]==True:
        offer =True
        offerlist=jd["offerlist"]
    else:
        offer =False
        offerlist=[]
    return render_template("index.html",avilableproduct=data,offer=offer,offerlist=offerlist) 



@roboapp.route("/tax/owner",methods=["GET","POST"])
def changetax():
    if request.method =="POST":
        id=request.form["id"]
        mpass=request.form["pass"]
        newtax=request.form["ntax"]
        with open("owner_d.json","r") as detail:
            m=json.load(detail)
        try:
            if m[id]["pass"]==mpass:
                taxd={"tax":newtax}
                with open("tax.json" ,"r")as mtax:
                    taxjson=json.load(mtax)
                try:
                    with open("tax.json" ,"w")as mtax:
                        json.dump(taxd,mtax)
                except:
                    with open("tax.json" ,"w")as mtax:
                        json.dump(taxjson,mtax)
                return "Dne"
        except:
            return "id pass not match"
        
    else:
        return '''<html><body><form action="/tax/owner" method="post"><br>
        Id"- <input type="text" name="id"><br> Password :- <input type="password" name="pass"> <br>Tax:-<input type="number" name="ntax"><br><input type="submit">'''

@roboapp.route("/submitproduct_payment/<tax>",methods=["POST","GET"])
@roboapp.route("/submitproduct_payment",methods=["POST","GET"])
@roboapp.route("/submitproduct_payment/<tax>/",methods=["POST","GET"])
@roboapp.route("/submitproduct_payment/",methods=["POST","GET"])
def submitproduct_payment(tax=None):
    with open("tax.json" ,"r")as mtax:
        taxjson=json.load(mtax)
        tax=taxjson["tax"]
    #if tax==None:
     #   tax=0
      #  tax__=tax
    if request.method =="POST":
        cname=request.form["cname"]
        cno=request.form["cno"]
        try:
            #tax=request.form["tax"]
            pass
            try:
                
                tax=int(tax)
            except:
                tax=18
        except:
            tax=18
        product_name=request.form.getlist("product[]")
        address=request.form["addr"]
        # {{i['count']}}
        # print(cname)
        # print(cno)
        # print(product_name)
        totalprise=0
        for i in product_name:
            totalprise +=rateof(i)
        qty=""
        for i in range(len(product_name)):
            qty +=str(1) + ","
        main_product=""
        for i in product_name:
            main_product +=str(i) + ","
        with open("invoice.json","r") as invoice__:
            invoice=json.load(invoice__)
            allinvoice=invoice
        while True:
            invoiceno= random.randint(100000,999999)
            if invoiceno not in allinvoice.keys():
                m_invoice=invoiceno
                break
        return render_template("payment.html",cname=cname,cno=cno,product_name=main_product,totalprise=totalprise,address=address,qty=qty,tax=tax,invoice=m_invoice)
    else :

        return redirect("/")


def rateof(item):
    with open("data.json","r") as hmmm:
        main_json=json.load(hmmm)
    return main_json[item]["prise"]




@roboapp.route("/getpaid/<invoice>",methods=["GET","POST"])    
@roboapp.route("/getpaid/<invoice>/",methods=["GET","POST"])    
def getpaid(invoice):
    # Request paytm to transfer the amount to your account after payment by user
    with open("invoice.json","r") as meandyou:
        youandme=json.load(meandyou)

    if youandme[str(invoice)]["status"].lower()!="paid":
        param_dict = {

                'MID': 'TirnwY02884048811102',
                'ORDER_ID': str(invoice),
                'TXN_AMOUNT': str(youandme[str(invoice)]["amount"]),
                'CUST_ID': str(youandme[str(invoice)]["cno"]),
                'INDUSTRY_TYPE_ID': 'Retail',
                'WEBSITE': 'WEBSTAGING',
                'CHANNEL_ID': 'WEB',
                'CALLBACK_URL':'http://192.168.43.181:8080/handlerequest/',

        }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return  render_template("paytm.html",param_dict=param_dict)
    else:
        return "your bill is paid"
    

@roboapp.route("/handlerequest",methods=["GET","POST"])
@roboapp.route("/handlerequest/",methods=["GET","POST"])
def handlerequest():
    # paytm will send you post request here
    form = request.form.to_dict()
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    with open("invoice.json","r") as read:
        myjsonread=json.load(read)
        mymain=myjsonread

    verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            # print('order successful')
            with open("invoice.json","w") as write:
                myjsonread[str(form["ORDERID"])]["status"]="Paid"
                myjsonread[str(form["ORDERID"])]["pmode"]="Paytm"
                try:
                    myjsonread[str(form["ORDERID"])]["transid"]=str(form["ORDERID"])
                except:
                    pass
                try:
                    json.dump(myjsonread,write)
                except:
                    json.dump(mymain,write)
                write.close()
        else:
            # print('order was not successful because' + response_dict['RESPMSG'])
            pass
    return render_template('paymentstatus.html', response= response_dict)

@roboapp.route("/peperback")
@roboapp.route("/peperback/")
def peperback():
    return send_from_directory(r'C:\Users\IamTheHimansh\Documents\BILLROPY\static',"images.jpg")



allinvoice={0:{"amount":9999,"tranc":"paid"}}


@roboapp.route("/getbill_pdf/<name>/<cno>/<addr>/<product>/<total>/<qty>/<m_invoice>",)
@roboapp.route("/getbill_pdf/<name>/<cno>/<addr>/<product>/<total>/<qty>/<m_invoice>/<tax>",)
@roboapp.route("/getbill_pdf/<name>/<cno>/<addr>/<product>/<total>/<qty>/<m_invoice>/<tax>/",)
@roboapp.route("/getbill_pdf/<name>/<cno>/<addr>/<product>/<total>/<qty>/<m_invoice>/",)
def getbill_pdf(name,cno,addr,product,total,qty,m_invoice,tax=None):
    # try:
    
    invoiceno=m_invoice   
    

    
    new0=[]
    new1=""
    for i in product:
        if product[product.find(i,0,len(product))]!=",":
            new1 +=i
        else:
            new0.append(new1)
            new1=""
    product=new0

    product1=[]
    for i in product:
        try:
            i=int(i)
            product1.append(i)
        except:
            pass

    product=product1
    new0=[]
    new1=""

    for i in qty:
        if qty[qty.find(i,0,len(qty))]!=",":
            new1 +=i
        else:
            new0.append(new1)
            new1=""
    qty=new0

    qty1=[]
    for i in qty:
        try:
            i=int(i)
            qty1.append(i)
        except:
            pass

    qty=qty1


    # name=request.form("cname")
    # cno=request.form("cco")
    # product=request.form.getlist("product")
    # addr=request.form("addr")
    if tax==None:
        tax=0
    allinvoice[f"{invoiceno}"]={"status":"Not paid","amount":int(total)*(100+int(tax))/100,"name":name,"addr":addr,"cno":cno,"product":product,"qty":qty,"date":str(date.today()),"tax":tax}
    with open("invoice.json","w") as upload:
        try:
            json.dump(allinvoice,upload)
        except:
            json.dump(invoice,upload)
    with open("data.json","r") as a:
        mjson=json.load(a)
    # print("1 done")
    if tax==None:
        tax=0
    renderd=render_template("invoice_tamplate.html",cname=name,cno=cno,addr=addr,product=product,total=total,invoice_no=m_invoice,date_c=date.today(),tax=tax,data=mjson,qty=qty)
    
    

    
    # pdf=pdfkit.from_string(renderd,False)
    # pdf=pdfkit.from_file(renderd,False)

    responce=make_response(renderd)
    
    # print("4 done")
    # responce.headers["Content-Type"]="application/pdf"

    
    # responce.headers["Content-Disposition"]="inline; filename=output.pdf"

    return responce
    # except Exception as e:
    #     print(e)
    #     return "failed to create bill"





@roboapp.route("/cheackinvoice",methods=["GET","POST"])
@roboapp.route("/cheackinvoice/",methods=["GET","POST"])
@roboapp.route("/cheackinvoice/<invoice>",methods=["GET","POST"])
@roboapp.route("/cheackinvoice/<invoice>/",methods=["GET","POST"])
@roboapp.route("/invoice/<invoice>",methods=["GET","POST"])
@roboapp.route("/invoice/",methods=["GET","POST"])
def cheackinvoice(invoice=None):
    maininvoicedata={}
    with open("invoice.json","r") as invoice_read:
        maininvoicedata=json.load(invoice_read)
    data={}
    with open("data.json","r") as data_read:
        data=json.load(data_read)

    invoicealert="<script>alert('Sorry Requested invoice not found')</script><center><strong>Sorry Requested invoice not found</strong></center>"
    try:
        if request.method.lower()=="post":

            invoice=request.form["invoice"]
        else:
            pass
    except Exception as  e:
        print(e)
        pass
    
    
    
    if invoice==None:
        if invoice==None:

            return render_template("invoicefill.html")
        else:
            myjson2={}
            with open("invoice.json","r") as json2:
                myjson2=json.load(json2)
            if invoice in myjson2.keys():
                return render_template("invoicemain.html",invoice_no=str(invoice),data=data,invoice=maininvoicedata)
            else:
                return invoicealert
    else:
        myjson2={}
        with open("invoice.json","r") as json2:
            myjson2=json.load(json2)
        if invoice in myjson2.keys():
            return render_template("invoicemain.html",invoice_no=str(invoice),data=data,invoice=maininvoicedata)
        else:
            return invoicealert





@roboapp.route("/veryfipay",methods=["POST","GET"])
@roboapp.route("/veryfipay/",methods=["GET","POST"])
def veryfipay():
    if request.method.lower() =="post":
        id_=request.form["id"]
        password=request.form["pass"]
        invoice=request.form["invoice"]
        paidto=request.form["paidto"]
        paidamount=request.form["paidamount"]
        transno=request.form["transid"]
        with open("idpass.json","r") as idpass_:
            idpass=json.load(idpass_)
        if idpass[id_]["pass"]==password:
            with open("invoice.json","r") as myinvoice:
                myinvoicedata=json.load(myinvoice)
                mybacupdata=myinvoicedata
                myinvoice.close()
            


            if str(myinvoicedata[invoice]["amount"])==str(paidamount):
                myinvoicedata[invoice]["status"]="Paid"
                myinvoicedata[invoice]["transid"]=str(transno)
                myinvoicedata[invoice]["paidto"]=str(paidto)
                myinvoicedata[invoice]["cheackedby"]=str(idpass[id_]["name"])
                # return redirect("/cheackinvoice/"+ invoice)
            else:
                myinvoicedata[invoice]["status"]="Not Paid"
                myinvoicedata[invoice]["transid"]=str(transno)
                myinvoicedata[invoice]["paidto"]=str(paidto)
                myinvoicedata[invoice]["cheackedby"]=str(idpass[id_["name"]])
                myinvoicedata[invoice]["restprise"]=str(int(myinvoicedata[invoice]["amount"])-int(paidamount))
                myinvoicedata[invoice]["paidamount"]=str(paidamount)
            with open("invoice.json","w") as writejson:
                try:
                    json.dump(myinvoicedata,writejson)
                except:
                    json.dump(mybacupdata,writejson)
            url="/cheackinvoice/"+ invoice
            return redirect(url)
        else:
            # return "Id pass Does not match <a href='/veryfipay'> try again</a> "
            return render_template("veryfipay.html",message="Id pass Does not match please try again")
    else:
        return render_template("veryfipay.html")



@roboapp.route("/logo",methods=["POST","GET"])
def logo():
    try:
        return send_from_directory(r"C:\Users\IamTheHimansh\Documents\BILLROPY\static\\","logo.jpg")
    except:
        return send_from_directory(r"C:\Users\IamTheHimansh\Documents\BILLROPY\static\\","logo.jpg")


@roboapp.route("/invoice/getamount",methods=["POST","GET"])
@roboapp.route("/invoice/getamount/",methods=["POST","GET"])
def getamount():
    if request.method.lower()=='post':
        invoice=request.form["invoice"]
        invoice=str(invoice)
        if invoice!="":
            with open("invoice.json",'r') as invoicedata:
                myinvoicedata=json.load(invoicedata)
            try:
                return   str("Amount :- " + str(myinvoicedata[invoice]["amount"]))
            except:
                return "Invalid Invoice No Plz  Cheack Again"
        else:
            return "Invoice no can't be blank"
    else:
        return '''
        <html>
        <head>
        </head>
        <body>
        <form action="/invoice/getamount" method="post">
        <br>
        Invoice no :-
        <input type="text" name="invoice"><br>
        <input type="submit">
        </form>
        </body>
        </html>
        '''



@roboapp.route("/loadinggif",methods=["POST","GET"])
@roboapp.route("/loadinggif/",methods=["POST","GET"])
def loadinggif():
    try:
        return send_from_directory("C:\\Users\\IamTheHimansh\\Documents\\BILLROPY\\static\\",'loading.gif')
    except:
        return send_from_directory("C:/Users/IamTheHimansh/Documents/BILLROPY/static/",'loading.gif')

@roboapp.route("/veryfypayany",methods=["POST","GET"])
@roboapp.route("/veryfypayany/",methods=["POST","GET"])
def veryfipayany():
    if request.method.lower() =="post":
        invoice=request.form["invoice"]
        paidamount=request.form["paidamount"]
        paidto=request.form["paidto"]
        transno=request.form["transid"]
        
        # with open("veryfyreq.json","r") as myinvoice:
        #     myinvoicedata=json.load(myinvoice)
        #     # mybacupdata=myinvoicedata
        #     myinvoice.close()
        # myinvoicedata[invoice]={"paidamount":paidamount,"paidto":paidto,"oderid":transno,"status":"Not Varified"}
        # paytm
        # paytmParams = dict()

        # paytmParams["MID"]     = "TirnwY02884048811102"
        # paytmParams["ORDERID"] = str(invoice)

        # # Generate checksum by parameters we have
        # # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
        # checksum = Checksum.generateSignature(paytmParams, MERCHANT_KEY)

        # paytmParams["CHECKSUMHASH"] = checksum

        # post_data = json.dumps(paytmParams)

        # for Staging
        # url = "https://securegw-stage.paytm.in/order/status"

        # for Production
        # url = "https://securegw.paytm.in/order/status"

        # responsesend = requests.post(url, data = post_data, )
        # response = requests.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
        # try:
        #     TXNID=responce[TXNID]
        # except:
        #     TXNID="Faild to get Transaction No"
        # try:
        #     responsesend__=str(json.dump(responsesend))
        # except:
        #     responsesend__="Feild To get"
        # end paytm
        try:
            # "open browser"
            # "open url"
            mymsg=f"-#'_* Check Payment *_'#-   \n  Invoice No:- {invoice} \n Paid Amount :- {paidamount} \n Paid To :- {paidto} \n Oder Id :- {transno} \n Transaction No. :- {transno} \n \n Veryfy Link :- http:/www.iamthehimansh.com/veryfypayagent"
            url="https://web.whatsapp.com/send?phone=+919939780504&amp;text&amp;source&amp;data&amp;app_absent"
                        # driver.execute_script(f"window.open('{{url}}')")
            driver.get(url)
            # sleep(1)
            inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
            inp_xpath=r'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
            sleep(10)
            input_box = driver.find_element_by_xpath(inp_xpath)
            # print("finded input box")
            sleep(2)
            # print("Sending key")
            input_box.send_keys(mymsg + Keys.ENTER)
            # print("Key sent")
            sleep(2)
            # driver.find_element_by_xpath().click()
            # driver.find_element_by_xpath(messagexpath).send_keys(mymsg)
            # driver.find_element_by_xpath(sendbtnxpath).click()
        except Exception as e:
            # print("Exception")
            print(e)
            return "Your data not sent plz try again"
        return "Your data sent to an agent wait 5 min To Veryfy"
    else:
        return render_template("veryfypayagentqrpay.html")

# verypay qr code payment self
@roboapp.route("/veryfypayagent",methods=["POST","GET"])
@roboapp.route("/veryfypayagent/",methods=["POST","GET"])
def veryfypayagent():
    if request.method.lower()=="post":
        invoice=request.form["invoice"]
        paidamount=request.form["cpaid"]
        sid=request.form["sid"]
        spass=request.form["spass"]
        # paidto=request.form["paidto"]
        # transno=request.form["transeid"]
        with open("idpass.json" ,"r") as idpass:
            idpassdata=json.load(idpass)
        if idpassdata[sid]["pass"]==spass:
            if str(invoice)!="" and str(paidamount) !=""  and paidamount!=None:
                with open("invoice.json","r") as myinvoice:
                    maininvoicedata=json.load(myinvoice)
                    backupdata=maininvoicedata
                try:
                    sname=idpassdata[sid]["name"]
                except:
                    sname="Invalid"
                try:
                    due=str(maininvoicedata[str(invoice)]["amount"])
                except:
                    due=None
                if str(maininvoicedata[str(invoice)]["amount"])==str(paidamount) or due!=paidamount:
                    if (maininvoicedata[str(invoice)]["status"]).lower()!="Paid".lower():
                        maininvoicedata[str(invoice)]["status"]="Paid"
                        maininvoicedata[str(invoice)]["pmode"]="Cash Staff"
                        maininvoicedata[str(invoice)]["sname"]=sname
                        maininvoicedata[str(invoice)]["due"]=0
                        if sname=="Invalid":
                            maininvoicedata[str(invoice)]["sid"]=sid

                    else:
                        return "Bill is paid earliar"
                else:
                    due=int(paidamount)-int(maininvoicedata[str(invoice)]["amount"])
                    maininvoicedata[str(invoice)]["Status"]="Not Paid"
                    maininvoicedata[str(invoice)]["pmode"]="Cash Staff"
                    maininvoicedata[str(invoice)]["sname"]=sname
                    maininvoicedata[str(invoice)]["due"]=due
                    if sname=="Invalid":
                        maininvoicedata[str(invoice)]["sid"]=sid
                try:
                    with open("invoice.json","w") as myinvoicesend:
                        json.dump(maininvoicedata,myinvoicesend)
                except:
                    with open("invoice.json","w") as myinvoicesend:
                        json.dump(backupdata,myinvoicesend)
                    return "Data Error"
                return "Pament Accepted"
            else:
                return "Send all data Error:- Data missing"
        else:
            return "Staff Id Pass Error"
    else:
        return render_template("veryfypayagent.html")

@roboapp.route("/paytmqrcode",methods=["POST","GET"])
@roboapp.route("/paytmqrcode/",methods=["POST","GET"])
def paytmqrcode():
    return send_from_directory(r"C:\Users\IamTheHimansh\Documents\BILLROPY\static","paytm.jpg")
@roboapp.route("/googlepayqrcode",methods=["POST","GET"])
@roboapp.route("/googlepayqrcode/",methods=["POST","GET"])
def googlepayqrcode():
    return send_from_directory(r"C:\Users\IamTheHimansh\Documents\BILLROPY\static","gpay.jpg")
@roboapp.route("/amazonpayqrcode",methods=["POST","GET"])
@roboapp.route("/amazonpayqrcode/",methods=["POST","GET"])
def amazonpayqrcode():
    return send_from_directory(r"C:\Users\IamTheHimansh\Documents\BILLROPY\static","paytm.jpg")
@roboapp.route("/phonepayqrcode",methods=["POST","GET"])
@roboapp.route("/phonepayqrcode/",methods=["POST","GET"])
def phonepayqrcode():
    return send_from_directory(r"C:\Users\IamTheHimansh\Documents\BILLROPY\static","phonepay.jpg")

@roboapp.route("/speak",methods=["GET","POST"])
def speak():
    if  request.method.lower()=="post":
        engine.say(str(request.form["text"]))
        engine.runAndWait()
        # {'id': 'robo 1.0','pass':'hamthumkonahijantayhai','text':a}
        if request.form["id"]=="robo 1.0" and request.form["pass"]=="hamthumkonahijantayhai":
            if request.form["text"]==None:
                pass
            else:
                engine.say(str(request.form["text"]))
                engine.runAndWait()
                print("..../------\____")
                with open("telltext.json","r") as tell:
                    mtell=json.load(tell)
                if type(mtell["tell"])==str:
                    with open("telltext.json","w")as wtell:
                        json.dump({"tell":[str(request.form["text"])]},wtell)
                        wtell.close()
                elif type(mtell["tell"])==list:
                    mtell["tell"].append(str(request.form["text"]))
                    uploaddata=mtell["tell"]
                    with open("telltext.json","w")as wtell:
                        json.dump({"tell":uploaddata},wtell)
                        wtell.close()
                else:
                    with open("telltext.json","w")as wtell:
                        json.dump({"tell":[str(request.form["text"])]},wtell)
                        wtell.close()
        return '''<a href='/speak'>click here to go back'''
    else:
        return """<center><form action='/speak' method='POST'>Id <input type='text' name='id'><br>Pass <input type='password' name='pass'><br>Text <input type='text' name='text'><br><input type='submit'>"""

@roboapp.route("/movement_json",methods=["GET","POST"])
def movment_json():
    if request.method.lower()=="post":
        if request.form["id"]=="robo 1.0" and request.form["pass"]=="@!@IamTheHimansh/robo1z":
            # with open(r"C:\Users\IamTheHimansh\Music\runit\go.json" ,"r") as go_file:
            
                # go_file.close() 
            data=callPersonAvilityCheacker()
            if data["person_avilable"]==False:
                count1.increase()
                data["person_not_avilabe_count"]=count1.get()
                person_frist_time.set(True)
                mystoped_obj.set(False)
                print("stoped: "+ str(mystoped_obj.get()))
            else:
                count1.zero()
                try:
                    data["frist_time"]=person_frist_time.get()
                except Exception as e:
                    print(e)
                    data["frist_time"]=False
                person_frist_time.set(False)



            # if mystoped_obj.get()==True:
            #     send_= {"movement":"go"}
            # elif mystoped_obj.get()==False:
            #     send_= {"movement":"stop"}



            go,stop__=auto_pilot_for_billropy.getinstruction(data,mystoped_obj.get())


            mystoped_obj.set(stop__)

            return go
        else:
            return {"status":"failed","code":1}
    else:
        return {"status":"failed","code":2}

@roboapp.route("/person_avilable.json",methods=["GET","POST"])
def person_avilable():
    if request.method.lower()=="post":
        # {"id":"robo 1.0","pass":"@!@IamTheHimansh/robo1z","data":person_avilable}
        if request.form["id"]=="robo 1.0" and request.form["pass"]=="@!@IamTheHimansh/robo1z":
            data=callPersonAvilityCheacker()
            if data["person_avilable"]==False:
                count1.increase()
                data["person_not_avilabe_count"]=count1.get()
                person_frist_time.set(True)
            else:
                count1.zero()
                try:
                    data["frist_time"]=person_frist_time.get()
                except Exception as e:
                    print(e)
                    data["frist_time"]=False
                person_frist_time.set(False)

            return data



@roboapp.route("/person_avilable.json/write",methods=["GET","POST"])
def person_avilable_write():
    return {"status":"temporary blocked"}
    # if request.method.lower()=="post":
    #     # {"id":"robo 1.0","pass":"@!@IamTheHimansh/robo1z","data":person_avilable}
    #     if request.form["id"]=="robo 1.0" and request.form["pass"]=="@!@IamTheHimansh/robo1z":
    #         if data["person_avilable"]==True:
    #             person_frist_time.set(data["frist_time"])
    #             return "done"
    #         else:
    #             return "failed code=1"
    #     else:
    #         return "failed code=2"
    # else:
    #     return "failed code=3"


@roboapp.route("/stoped/kle")
def stoped():
    if mystoped_obj.get()==True:
        return {"movement":"stop"}
    elif mystoped_obj.get()==False:
        return {"movement":"go"}
    else:
        return f"{mystoped_obj.get()}"

@roboapp.route("/stoped/write/<password>/<info>")
def w_stoped(password,info):
    if password=="cvb@!#himansh.robo.com":
        if info=="go":
            mystoped_obj.set(False)
        elif info=="stop":
            mystoped_obj.set(True)
        return "done"
    else:
        "failed"
if __name__ == "__main__":
    roboapp.run(debug=True)
    #serve(roboapp, host='0.0.0.0', port=8080, threads=1) #WAITRESS!
    #callwhtappscan()
