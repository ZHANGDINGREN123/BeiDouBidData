#coding=utf-8

from flask import Flask,render_template,request
from Dao import FirstLayer
from Dao import DepartmHandResult
from Dao1 import Second_Layer,Second_DepartmHandResult
from Dao2 import Third_Layer,Third_DepartmHandResult
from Dao3 import Fourth_Layer,Fourth_DepartmHandResult
from Table_Show import Security_Table_Show,Fault_Table_Show
from Word_Cloud import security_word_cloud,falut_word_cloud
from New import new_fault,new_security
from Fault_Dashboard import fault_dashboad,fault_dashboard4,fault_dashboard5,security_dashboard,security_dashboard2,security_dashboard3,security_dashboard4,security_dashboard5

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    if request == 'GET':
        return render_template("index.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Hand_Result = request.form.get('Hand_Result')
        EmployerCode = request.form.get('Department_Type')
        Responsibli_Preson = request.form.get('Responsibli_Preson')
        Show_S_RESPONSIBILITYDEPT = DepartmHandResult.first_layer_Two('2017-07-22', '2017-08-23')
        show_S_HANDLEREASULT = FirstLayer.first_layer(dateBegin,dateEnd)
        show_S_Second_Layer_RESPONSIBILITYDEPT,show_S_Second_Layer_Hand_Result= Second_Layer.Second_layer(dateBegin,dateEnd,Hand_Result)
        show_S_Third_Layer_S_EMPLOYEECODE,show_S_Third_Layer_EmployerCode= Third_Layer.Third_layer(dateBegin,dateEnd,Hand_Result,EmployerCode)
        show_S_Fourth_Layer_RESPONSIBLEPERSON,show_S_Fourth_Layer_People_Depart = Fourth_Layer.Fourth_layer(dateBegin,dateEnd,Hand_Result,EmployerCode,Responsibli_Preson)
        return render_template('index.html',dateBegin = dateBegin,
                               dateEnd = dateEnd,
                               Show_S_RESPONSIBILITYDEPT = Show_S_RESPONSIBILITYDEPT, show_S_HANDLEREASULT = show_S_HANDLEREASULT,show_S_Second_Layer_RESPONSIBILITYDEPT = show_S_Second_Layer_RESPONSIBILITYDEPT,show_S_Second_Layer_Hand_Result = show_S_Second_Layer_Hand_Result,show_S_Third_Layer_S_EMPLOYEECODE = show_S_Third_Layer_S_EMPLOYEECODE,show_S_Third_Layer_EmployerCode=show_S_Third_Layer_EmployerCode,show_S_Fourth_Layer_RESPONSIBLEPERSON = show_S_Fourth_Layer_RESPONSIBLEPERSON,show_S_Fourth_Layer_People_Depart=show_S_Fourth_Layer_People_Depart)


@app.route('/init',methods=['GET', 'POST'])
def init():
    if request == 'GET':
        return render_template("init1.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Hand_Result = request.form.get('Hand_Result')
        EmployerCode = request.form.get('Department_Type')
        Responsibli_Preson = request.form.get('Responsibli_Preson')
        Show_S_RESPONSIBILITYDEPT = DepartmHandResult.first_layer_Two(dateBegin, dateEnd)
        show_S_HANDLEREASULT = FirstLayer.first_layer(dateBegin, dateEnd)
        show_S_Second_Layer_RESPONSIBILITYDEPT = Second_Layer.Second_layer(dateBegin, dateEnd, Hand_Result)
        show_S_Third_Layer_S_EMPLOYEECODE = Third_Layer.Third_layer(dateBegin, dateEnd, Hand_Result, EmployerCode)
        show_S_Fourth_Layer_RESPONSIBLEPERSON = Fourth_Layer.Fourth_layer(dateBegin, dateEnd, Hand_Result, EmployerCode,
                                                                          Responsibli_Preson)
        return render_template('init1.html',Show_S_RESPONSIBILITYDEPT=Show_S_RESPONSIBILITYDEPT,
                               show_S_HANDLEREASULT=show_S_HANDLEREASULT,
                               show_S_Second_Layer_RESPONSIBILITYDEPT=show_S_Second_Layer_RESPONSIBILITYDEPT,
                               show_S_Third_Layer_S_EMPLOYEECODE=show_S_Third_Layer_S_EMPLOYEECODE,
                               show_S_Fourth_Layer_RESPONSIBLEPERSON=show_S_Fourth_Layer_RESPONSIBLEPERSON)
@app.route('/index2',methods=['GET', 'POST'])
def index2():
    if request == 'GET':
        return render_template("index.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Check_Department = request.form.get('Check_Department')
        Hand_Result = request.form.get('Hand_Result')
        Responsibli_Code_two = request.form.get('Responsibli_Code_two')
        Show_S_RESPONSIBILITYDEPT,_ = Fourth_DepartmHandResult.Fourth_Layer_Two(dateBegin, dateEnd)
        show_S_Second_Layer_Two_Check_Department,show_S_Second_Layer__Two_Check_Department1= Fourth_DepartmHandResult.Fourth_Layer_Two(dateBegin, dateEnd,Check_Department)
        show_S_Third_Layer_S_Hand_Result,show_S_Third_Layer_S_Hand_Result1= Fourth_DepartmHandResult.Fourth_Layer_Two(dateBegin,dateEnd,Check_Department,Hand_Result)
        show_S_Fourth_Layer_People_Code,show_S_Fourth_Layer_People_Code1 = Fourth_DepartmHandResult.Fourth_Layer_Two(dateBegin,dateEnd,Check_Department,Hand_Result,Responsibli_Code_two)
        # return render_template('index2.html',Show_S_RESPONSIBILITYDEPT = Show_S_RESPONSIBILITYDEPT, show_S_HANDLEREASULT = show_S_HANDLEREASULT,show_S_Second_Layer_RESPONSIBILITYDEPT = show_S_Second_Layer_RESPONSIBILITYDEPT,show_S_Second_Layer_Hand_Result = show_S_Second_Layer_Hand_Result,show_S_Third_Layer_S_EMPLOYEECODE = show_S_Third_Layer_S_EMPLOYEECODE,show_S_Third_Layer_EmployerCode=show_S_Third_Layer_EmployerCode,show_S_Fourth_Layer_RESPONSIBLEPERSON = show_S_Fourth_Layer_RESPONSIBLEPERSON,show_S_Fourth_Layer_People_Depart=show_S_Fourth_Layer_People_Depart)
        return render_template('index2.html',dateBegin = dateBegin,
                               dateEnd = dateEnd,
                               Show_S_RESPONSIBILITYDEPT = Show_S_RESPONSIBILITYDEPT,
                               show_S_Second_Layer_Two_Check_Department = show_S_Second_Layer_Two_Check_Department,
                               show_S_Second_Layer__Two_Check_Department1 = show_S_Second_Layer__Two_Check_Department1,
                               show_S_Third_Layer_S_Hand_Result = show_S_Third_Layer_S_Hand_Result,
                               show_S_Third_Layer_S_Hand_Result1 = show_S_Third_Layer_S_Hand_Result1,
                               show_S_Fourth_Layer_People_Code = show_S_Fourth_Layer_People_Code,
                               show_S_Fourth_Layer_People_Code1 = show_S_Fourth_Layer_People_Code1)

@app.route('/faultyDashboard',methods=['GET', 'POST'])
def faultyDashboard():
    if request == 'GET':
        return render_template("faultyDashboard.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        # show_S_Security_Word = security_word_cloud.Security_Word_Cloud(dateBegin,dateEnd)
        show_S_new_falut = new_fault.new_fault_show(dateBegin,dateEnd)
        show_S_Falut_Word = falut_word_cloud.Fault_Word_Cloud(dateBegin,dateEnd)
        Dashboard1 = fault_dashboad.show_fault_dashboard(dateBegin,dateEnd)
        Dashboard2 = sorted(falut_word_cloud.Fault_Word_Cloud(dateBegin, dateEnd), key=lambda x: (falut_word_cloud.Fault_Word_Cloud(dateBegin, dateEnd))[x])[-1]
        Dashboard3 = sorted(falut_word_cloud.Fault_Word_Cloud(dateBegin, dateEnd), key=lambda x: (falut_word_cloud.Fault_Word_Cloud(dateBegin, dateEnd))[x])[-2]
        Dashboard4 = fault_dashboard4.show_fault_dashboard4(dateBegin,dateEnd)
        Dashboard5 = fault_dashboard5.show_fault_dashboard5(dateBegin,dateEnd)
    return render_template('faultyDashboard.html',
                            dateBegin = dateBegin,
                            dateEnd = dateEnd,
                            show_S_new_falut = show_S_new_falut,
                            show_S_Falut_Word = show_S_Falut_Word,
                            Dashboard2 = Dashboard2,
                            Dashboard1 = Dashboard1,
                            Dashboard3 = Dashboard3,
                            Dashboard4=Dashboard4,
                            Dashboard5=Dashboard5
                           )


@app.route('/securityDashboard', methods=['GET', 'POST'])
def securityDashboard():
    if request == 'GET':
        return render_template('securityDashboard.html')
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        Security1 = security_dashboard.show_security_dashboard1(dateBegin, dateEnd)
        Security2 = security_dashboard2.show_security_dashboard2(dateBegin, dateEnd)
        Security3 = security_dashboard3.show_security_dashboard3(dateBegin, dateEnd)
        Security4 = security_dashboard4.show_security_dashboard4(dateBegin, dateEnd)
        Security5 = security_dashboard5.show_security_dashboard5(dateBegin, dateEnd)
        show_S_Security_Word = security_word_cloud.Security_Word_Cloud(dateBegin, dateEnd)
        show_S_new_security = new_security.new_security_show(dateBegin, dateEnd)
    return render_template('securityDashboard.html',
                           dateBegin=dateBegin,
                           dateEnd=dateEnd,
                           show_S_new_security = show_S_new_security,
                           show_S_Security_Word=show_S_Security_Word,
                           Security1 =Security1,
                            Security2 = Security2,
                            Security3 = Security3,
                            Security4 = Security4,
                            Security5 = Security5)


@app.route('/punchDashboard',)
def punchDashboard():
    return render_template('punchDashboard.html')

@app.route('/tableFault',methods=['GET', 'POST'])
def tableFault():
    if request == 'GET':
        return render_template("table_fault.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        show_S_Fault_Table = Fault_Table_Show.fault_table_show(dateBegin, dateEnd)
    return render_template('table_fault.html',
                           show_S_Fault_Table=show_S_Fault_Table,
                           dateBegin = dateBegin,
                           dateEnd = dateEnd)

@app.route('/tableSecurity',methods=['GET', 'POST'])
def tableSecurity():
    if request == 'GET':
        return render_template("table_security.html")
    else:
        dateBegin = request.form.get('Date_Begin')
        dateEnd = request.form.get('Date_End')
        show_S_Security_Table = Security_Table_Show.security_table_show(dateBegin,dateEnd)
    return render_template('table_security.html',
                           show_S_Security_Table = show_S_Security_Table,
                           dateBegin=dateBegin,
                           dateEnd=dateEnd
                           )

@app.route('/tablePunch',)
def tablePunch():
    return render_template('table_punch.html')



if __name__ == '__main__':
    app.run(debug=False,host='172.21.176.74',port=5000)