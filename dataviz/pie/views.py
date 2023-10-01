from django.shortcuts import render
from . models import Empcomp
import numpy as np
import plotly.express as px

def index(request):
    context = {}  # Initialize an empty context dictionary
    
    if request.method == 'POST':
        columns = ['total_salary', 'retirement', 'health_and_dental', 'other_benefits', 'total_benefits', 'total_compensation']
        emp = request.POST.get('empid')
        
        if emp:
            data = Empcomp.objects.filter(employee_identifier=emp).values('total_salary','retirement','health_and_dental','other_benefits','total_benefits','total_compensation')
            # Rest of your data processing
            sal = []
            ret = []
            hd = []
            obe = []
            be = []
            comp = []
            for i in data:
                for j in columns:
                    if j=='total_salary':
                        sal.append(i[j])
                    elif j=='retirement':
                        ret.append(i[j])
                    elif j=='health_and_dental':
                        hd.append(i[j])
                    elif j=='other_benefits':
                        obe.append(i[j])
                    elif j=='total_benefits':
                        be.append(i[j])
                    elif j=='total_compensation':
                        comp.append(i[j])

            
            # print(sal, ret, obe, be, hd, comp)

        vals = []
        for i in ([sal, ret, hd, obe, be, comp]):
            vals.append(round(np.mean(i), 2))

        # Pie Chart Data

        colnames = ['Salary', 'Retirement', 'Health and Dental Benifits', 'Other Benifits', 'Benifits']
        colvals = vals[0:5]
        compval = vals[5]

        colperc = []

        for i in colvals:
            colperc.append((i/compval)*100)

        # Pie Chart
        tname = "Compensation Details of Employee: "+ emp
        fig = px.pie(values=colperc, names=colnames, title=tname)
        fig.update_traces(hoverinfo='name+percent', textinfo='percent')
        fig.update_layout(autosize=False,width=550,height=550)
        chart = fig.to_html()

        
            # Create the context dictionary
        context = {'graph': chart}

    return render(request, 'index.html', context)  # Pass the context to the render function
