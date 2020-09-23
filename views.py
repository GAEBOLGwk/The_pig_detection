from django.http import HttpResponse
from django.shortcuts import render,redirect
from dateapp import models
import  os
import os.path
from dateapp.my_dict import label_dict_HB,label_dict_O,label_dict_K
# Create your views here.
def login (request):
    if request.method=='GET':
        return render(request,'login.html')
    elif request.method=='POST':
        # print('d')
        u = request.POST.get("user")
        p = request.POST.get("pswd")
        obj = models.pig_web_info.objects.filter(user=u, password=p).first()
        if obj:
            # print('qq')
            # return render(request, 'index.html')
            return redirect("/index/")

        else:
            return render(request, "index.html")


def index (request):
    return render(request,'index.html')

def basic(request):
    return render(request,'basic.html')

def basicshow(request):
    Pigid =request.POST.get('Pigid')
    Birthdate= request.POST.get('Birthdate')
    Weight = request.POST.get('Weight')
    s= request.POST.get('s')
    y= request.POST.get('y')
    j = request.POST.get('j')
    # print('qqq')
    models.pig_Info.objects.create(Pigid=Pigid,Birthdate=Birthdate,Weight = Weight ,Fodder=s,Vaccine=y,Disease=j)
    return render(request, 'basic.html')
    # return HttpResponse('ok')

def user_info (request):
    if request.method=="GET":
        list=models.pig_watchdog_info.objects.all()
        return render(request,"user_info.html",{"list":list})
    elif request.method=="POST":
        u=request.POST.get("username")
        models.pig_watchdog_info.objects.create(name=u)
        return  redirect("/user_info/")
def user_info_d (request):
    if request.method=="GET":
        list=models.pig_watchdog_info_d.objects.all()
        return render(request,"user_info_d.html",{"list":list})
    elif request.method=="POST":
        u=request.POST.get("username")
        models.pig_watchdog_info_d.objects.create(name=u)
        return  redirect("/user_info_d/")

from itertools import groupby
def userdetail (request,nid):

    max_list=[]
    # D_HB_list = []
    # D_K_list = []
    # D_O_list = []
    if request.method=="GET":
        for parent, dirnames, filenames in os.walk("./static/pig_database"):
            print(parent)
            print(dirnames)
            print(filenames)


            if parent=='./static/pig_database':
                continue
            min_list = []
            HB_list = []
            K_list = []
            O_list = []


            #     for obj in filenames:
            #         print(obj)
            #         o_name = obj.split(".")[0]
            #         if obj.split(".")[-1] == 'txt':
            #             f = open(parent + '\\' + obj, 'r')
            #             content = f.read().splitlines()
            #             print(content)
            #             if '#' in content:
            #                 result = [list(g) for k, g in groupby(content, lambda x: x == '#') if not k]
            #                 del result[0]
            #
            #                 for l in result:
            #                     if o_name.split('_')[-1] == 'HB':
            #                         # print("xxxx",type(content[-2]))
            #                         # print(label_dict_HB)
            #                         l[-2]=((label_dict_HB[0])[l[-2]])
            #                         D_HB_list.append(l)
            #
            #                     elif o_name.split('_')[-1] == 'O':
            #                         l[-2] = ((label_dict_O[0])[l[-2]])
            #                         D_O_list.append(l)
            #                     elif o_name.split('_')[-1] == 'K':
            #                         l[-2] = ((label_dict_K)[l[-2]])
            #                         D_K_list.append(l)
            #             else:
            #                 del content[0]
            #                 if o_name.split('_')[-1] == 'HB':
            #                     # print("xxxx",type(content[-2]))
            #                     # print(label_dict_HB)
            #                     content[-2] = ((label_dict_HB[0])[content[-2]])
            #                     D_HB_list.append(content)
            #
            #                 elif o_name.split('_')[-1] == 'O':
            #                     content[-2] = ((label_dict_O[0])[content[-2]])
            #                     D_O_list.append(content)
            #                 elif o_name.split('_')[-1] == 'K':
            #                     content[-2] = ((label_dict_K)[content[-2]])
            #                     D_K_list.append(content)
            #
            #
            #         elif obj.split(".")[-1] == 'jpg':
            #             if o_name.split('_')[-1] == 'HB':
            #                 D_HB_list.append("#")
            #                 D_HB_list.append(parent + '//' + obj)
            #             elif o_name.split('_')[-1] == 'O':
            #                 D_O_list.append("#")
            #                 D_O_list.append(parent + '//' + obj)
            #             elif o_name.split('_')[-1] == 'K':
            #                 D_K_list.append("#")
            #                 D_K_list.append(parent + '//' + obj)
            #         # print("xxx",D_O_list)

            if 'DD' not in parent.split('\\')[-1]:
                for obj in filenames:
                    print(obj)
                    o_name=obj.split(".")[0]
                    if obj.split(".")[-1]=='txt':
                        f=open(parent+'\\'+obj,'r')
                        content=f.read().splitlines()
                        print(content)
                        if o_name.split('_')[-1]=='HB':
                            # print("xxxx",type(content[-2]))
                            # print(label_dict_HB)
                            HB_list.append((label_dict_HB[0])[content[-2]])
                            HB_list.append(content[-1])
                        elif o_name.split('_')[-1]=='O':
                            O_list.append(label_dict_O[0][content[-2]])
                            O_list.append(content[-1])

                        elif o_name.split('_')[-1]=='K':
                            K_list.append(label_dict_K[content[-2]])
                            K_list.append(content[-1])

                    elif obj.split(".")[-1]=='jpg':
                        if o_name.split('_')[-1] == 'HB':
                            HB_list.append(parent+'//'+obj)
                        elif o_name.split('_')[-1] == 'O':
                            O_list.append(parent+'//'+obj)
                        elif o_name.split('_')[-1] == 'K':
                            K_list.append(parent+'//'+obj)
                min_list.append(HB_list)
                min_list.append(O_list)
                min_list.append(K_list)
                max_list.append(min_list)
        # print(HB_list)
        # print()
        # print(O_list)
        # print()
        # print(K_list)
        print(max_list)
        return render(request, "user_detail.html", {"max_list": max_list,'nid':nid})


def pigdetail (request,nid):

    D_HB_list = []
    D_K_list = []
    D_O_list = []
    if request.method=="GET":
        for parent, dirnames, filenames in os.walk("./static/pig_database"):
            print(parent)
            print(dirnames)
            print(filenames)


            if parent=='./static/pig_database':
                continue

            if  'DD' in parent.split('\\')[-1]:
                for obj in filenames:
                    print(obj)
                    o_name = obj.split(".")[0]
                    if obj.split(".")[-1] == 'txt':
                        f = open(parent + '\\' + obj, 'r')
                        content = f.read().splitlines()
                        print(content)
                        if '#' in content:
                            result = [list(g) for k, g in groupby(content, lambda x: x == '#') if not k]
                            del result[0]

                            for l in result:
                                if o_name.split('_')[-1] == 'HB':

                                    l[-2]=((label_dict_HB[0])[l[-2]])
                                    D_HB_list.append(l)

                                elif o_name.split('_')[-1] == 'O':
                                    l[-2] = ((label_dict_O[0])[l[-2]])
                                    D_O_list.append(l)
                                elif o_name.split('_')[-1] == 'K':
                                    l[-2] = ((label_dict_K)[l[-2]])
                                    D_K_list.append(l)
                        else:
                            del content[0]
                            if o_name.split('_')[-1] == 'HB':
                                # print("xxxx",type(content[-2]))
                                # print(label_dict_HB)
                                content[-2] = ((label_dict_HB[0])[content[-2]])
                                D_HB_list.append(content)

                            elif o_name.split('_')[-1] == 'O':
                                content[-2] = ((label_dict_O[0])[content[-2]])
                                D_O_list.append(content)
                            elif o_name.split('_')[-1] == 'K':
                                content[-2] = ((label_dict_K)[content[-2]])
                                D_K_list.append(content)


                    elif obj.split(".")[-1] == 'jpg':
                        if o_name.split('_')[-1] == 'HB':
                            D_HB_list.append(parent + '//' + obj)
                        elif o_name.split('_')[-1] == 'O':
                            D_O_list.append(parent + '//' + obj)
                        elif o_name.split('_')[-1] == 'K':
                            D_K_list.append(parent + '//' + obj)
                    # print("xxx",D_O_list)
        print("#",D_HB_list)
        print("##",D_O_list)
        print("###",D_K_list)
        return render(request, "pigdetail.html",
                          {'nid': nid, "D_HB_list": D_HB_list, 'D_O_list': D_O_list, "D_K_list": D_K_list})
        #     for obj in filenames:
        #         print(obj)
        #         o_name=obj.split(".")[0]
        #         if obj.split(".")[-1]=='txt':
        #             f=open(parent+'\\'+obj,'r')
        #             content=f.read().splitlines()
        #             print(content)
        #             # if '#' in content:
        #             #     result = [list(g) for k, g in groupby(content, lambda x: x == '#') if not k]
        #             #     del result[0]
        #             #     print(result)
        #             #     for l in result:
        #             #         l[]((label_dict_HB[0])[l[-2]])
        #             #         D_HB_list.append(l)
        #             if o_name.split('_')[-1]=='HB':
        #                 # print("xxxx",type(content[-2]))
        #                 # print(label_dict_HB)
        #                 HB_list.append((label_dict_HB[0])[content[-2]])
        #                 HB_list.append(content[-1])
        #             elif o_name.split('_')[-1]=='O':
        #                 O_list.append(label_dict_O[0][content[-2]])
        #                 O_list.append(content[-1])
        #
        #             elif o_name.split('_')[-1]=='K':
        #                 K_list.append(label_dict_K[content[-2]])
        #                 K_list.append(content[-1])
        #
        #         elif obj.split(".")[-1]=='jpg':
        #             if o_name.split('_')[-1] == 'HB':
        #                 HB_list.append(parent+'//'+obj)
        #             elif o_name.split('_')[-1] == 'O':
        #                 O_list.append(parent+'//'+obj)
        #             elif o_name.split('_')[-1] == 'K':
        #                 K_list.append(parent+'//'+obj)
        #     min_list.append(HB_list)
        #     min_list.append(O_list)
        #     min_list.append(K_list)
        #     max_list.append(min_list)
        # # print(HB_list)
        # # print()
        # # print(O_list)
        # # print()
        # # print(K_list)
        # print(max_list)
        # print("#",D_HB_list)
        # print("##",D_O_list)
        # print("###",D_K_list)

def interactivate (request):
    p=1
    import os
    import shutil
    shutil.rmtree('upload')
    os.mkdir('upload')
    list = models.pig_watchdog_info.objects.all()
    if request.method=="GET":

        return render(request,"interactivate.html",{"list":list})
    if request.method == "POST":
        v1=request.POST.get("inlineRadioOptions")
        print(v1)
        v2=request.POST.getlist("jsq")
        print(v2)
        v = request.FILES.get("ffff")
        if v1==None or v2==None or v==None:
            return render(request, "interactivate.html", {"list": list})

        print(v, type(v), v.name)
        import os
        path = os.path.join("upload", v.name)
        print(path)
        f = open(path, mode="wb")
        for i in v.chunks():
            f.write(i)
        f.close()
        ROW="python my_infer.py %s %s %s"%(path.replace('\\','/'),v2[0],v1)
        p = os.system(ROW)
        print(p)
        return render(request,'interactivate.html',{'p':p,})