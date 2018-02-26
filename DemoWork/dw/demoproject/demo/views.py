from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from django.core.urlresolvers import reverse
import pandas
import json

from .fusioncharts import FusionCharts

from .forms import DocumentForm
# Create your views here.





def home(request):
  data = open("media/documents/rlData.json").read()

  data = json.loads(data)

  data1 = open("media/documents/rlDateCreated.json").read()

  data1 = json.loads(data1)


  data2 = open("media/documents/rlDateCompleted.json").read()

  data2 = json.loads(data2)


  data3 = open("media/documents/rlDateRevised.json").read()

  data3 = json.loads(data3)





  chart = FusionCharts("doughnut2d", "ex1" , "500", "400", "chart-1", "json",

  {
    "chart": {
        "caption": "Data Comparison - Jarowinkler Method",
        "subcaption": "Record Linkage based on Title , Date Created , Date Completed and Revised",
        "startingangle": "310",
        "decimals": "2",
        "defaultcenterlabel": "Result",
        "centerlabel": "$value%",
        "theme": "fint"
    },
    "data": [
        {
            "label": "Title",
            "value": ((data["Jarowinkler - Method"]["mean"])*100)
            
        },
        {
            "label": "Date Created",
            "value": ((data1["Jarowinkler - Method"]["mean"])*100)
        },
        {
            "label": "Date Completed",
            "value": ((data2["Jarowinkler - Method"]["mean"])*100)
        },
        {
            "label": "Date Revised",
            "value": ((data3["Jarowinkler - Method"]["mean"])*100)
        }
    ]
})





  




  chart1 = FusionCharts("doughnut2d", "ex2" , "500", "400", "chart-2", "json",

  {
    "chart": {
        "caption": "Data Comparison - Levenshtein Method",
        "subcaption": "Record Linkage based on Title , Date Created , Date Completed and Revised",
        "startingangle": "130",
        "decimals": "2",
        "defaultcenterlabel": "Result",
        "centerlabel": "$value%",
        "theme": "fint"
    },
    "data": [
        {
            "label": "Title",
            "value": ((data["Levenshtein - Method"]["mean"])*100)
            
        },
        {
            "label": "Date Created",
            "value": ((data1["Levenshtein - Method"]["mean"])*100)
        },
        {
            "label": "Date Completed",
            "value": ((data2["Levenshtein - Method"]["mean"])*100)
        },
        {
            "label": "Date Revised",
            "value": (data3["Levenshtein - Method"]["mean"])*100
        }
    ]
})


  return render(request,'demo/home.html',{
      'countTitle': "%d" % ((data["Jarowinkler - Method"]["count"])),
		  'jmeanTitle' : "%.2f%%" % ((data["Jarowinkler - Method"]["mean"])*100 ),
		  'lmeanTitle': "%.2f%%" % ((data['Levenshtein - Method']["mean"])*100),
		  'lminTitle' : "%.2f%%" % ((data['Levenshtein - Method']["min"])*100),
		  'lmaxTitle' : "%.2f%%" % ((data['Levenshtein - Method']["max"])*100),
		  'jminTitle' : "%.2f%%" % ((data["Jarowinkler - Method"]["min"])*100 ),
		  'jmaxTitle' : "%.2f%%" % ((data["Jarowinkler - Method"]["max"])*100 ),

      'countDC': "%d" % ((data1["Jarowinkler - Method"]["count"])),
      'jmeanDC' : "%.2f%%" % ((data1["Jarowinkler - Method"]["mean"])*100 ),
      'lmeanDC': "%.2f%%" % ((data1['Levenshtein - Method']["mean"])*100),
      'lminDC' : "%.2f%%" % ((data1['Levenshtein - Method']["min"])*100),
      'lmaxDC' : "%.2f%%" % ((data1['Levenshtein - Method']["max"])*100),
      'jminDC' : "%.2f%%" % ((data1["Jarowinkler - Method"]["min"])*100 ),
      'jmaxDC' : "%.2f%%" % ((data1["Jarowinkler - Method"]["max"])*100 ),


      'countDE': "%d" % ((data2["Jarowinkler - Method"]["count"])),
      'jmeanDE' : "%.2f%%" % ((data2["Jarowinkler - Method"]["mean"])*100 ),
      'lmeanDE': "%.2f%%" % ((data2['Levenshtein - Method']["mean"])*100),
      'lminDE' : "%.2f%%" % ((data2['Levenshtein - Method']["min"])*100),
      'lmaxDE' : "%.2f%%" % ((data2['Levenshtein - Method']["max"])*100),
      'jminDE' : "%.2f%%" % ((data2["Jarowinkler - Method"]["min"])*100 ),
      'jmaxDE' : "%.2f%%" % ((data2["Jarowinkler - Method"]["max"])*100 ),



      'countDR': "%d" % ((data3["Jarowinkler - Method"]["count"])),
      'jmeanDR' : "%.2f%%" % ((data3["Jarowinkler - Method"]["mean"])*100 ),
      'lmeanDR': "%.2f%%" % ((data3['Levenshtein - Method']["mean"])*100),
      'lminDR' : "%.2f%%" % ((data3['Levenshtein - Method']["min"])*100),
      'lmaxDR' : "%.2f%%" % ((data3['Levenshtein - Method']["max"])*100),
      'jminDR' : "%.2f%%" % ((data3["Jarowinkler - Method"]["min"])*100 ),
      'jmaxDR' : "%.2f%%" % ((data3["Jarowinkler - Method"]["max"])*100 ),

      'chart' : chart.render(),
      'chart1': chart1.render(),
      
		})

def model_form_upload(request):

#	file = open ("media/documents/AAA.json").read()

	print(file)
	if request.method == "POST":
		form = DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('home'))

	else:
		form = DocumentForm()

	return render(request,'demo/simple_upload.html',{'form':form})


def chart(request):
      # Create an object for the column2d chart using the FusionCharts class constructor
  

  

  column2d1 = FusionCharts("column3d", "ex1" , "500", "400", "chart-1", "json", 
          # The data is passed as a string in the `dataSource` as parameter.
      """{  
            "chart":{  
              "caption":"Pubmed Article",
              "subCaption":"No of Articles Created for years",
              "theme":"zune"
              
              
            },
            "data":[  
              {"label":"2005", "value":"298"},
              {"label":"2006", "value":"2718"},
              {"label":"2007", "value":"1194"},
              {"label":"2008", "value":"1151"},
              {"label":"2009", "value":"1576"},
              {"label":"2010", "value":"279"},
              {"label":"2011", "value":"269"},
              {"label":"2012", "value":"128"},
              {"label":"2013", "value":"11774"},
              {"label":"2014", "value":"2260"},
              {"label":"2015", "value":"1678"},
              {"label":"2016", "value":"3172"},
              {"label":"2017", "value":"0"},
            ],

        }""")


  column2d2 = FusionCharts("column3d", "ex2" , "500", "400", "chart-2", "json", 
          # The data is passed as a string in the `dataSource` as parameter.
      """{  
            "chart":{  
              "caption":"Clinical Trials",
              "subCaption":"No of Clinical Trials Conducted",
              
              
            },
            "data":[  
              {"label":"2005", "value":"840"},
              {"label":"2006", "value":"36"},
              {"label":"2007", "value":"36"},
              {"label":"2008", "value":"629"},
              {"label":"2009", "value":"153"},
              {"label":"2010", "value":"194"},
              {"label":"2011", "value":"181"},
              {"label":"2012", "value":"681"},
              {"label":"2013", "value":"1110"},
              {"label":"2014", "value":"230"},
              {"label":"2015", "value":"309"},
              {"label":"2016", "value":"802"},
              {"label":"2017", "value":"555"},
            ],

        }""")

      # returning complete JavaScript and HTML code, which is used to generate chart in the browsers. 
  

  chart1 = FusionCharts("mscolumn2d", "ex3" , "800", "600", "chart-3", "json", 
    """{
    "chart": 
    {
        "caption": "Pubmed and Clinical Trials Data",
        "subcaption": "No of Articles/Clinical Trials Created during 2005-2017",
        "yaxismaxvalue": "13000",
        "decimals": "0",
        "numberprefix": "",
        "numbersuffix": "",
        "placevaluesinside": "1",
        "valuefontbold": "1",
        "rotatevalues": "0",
        "divlinealpha": "50",
        "plotfillalpha": "80",
        "bgcolor": "FFFFFF",
        "theme": "zune"
    },
    "categories": 
    [
        {
            "category": [
                {
                    "label": "2005"
                },
                {
                    "label": "2006"
                },
                {
                    "label": "2007"
                },
                {
                    "label": "2008"
                },
                {
                    "label":"2009"
                },
                {
                    "label":"2010"
                },
                {
                    "label":"2011"
                },
                {
                    "label":"2012"
                },
                {
                    "label":"2013"
                },
                {
                    "label":"2014"
                },
                {
                    "label":"2015"
                },
                {
                    "label":"2016"
                },
                {
                    "label":"2017"
                },
            ]
        }
    ],
    "dataset": [
        {
            "seriesname": "pubmed",
            "data": [
                {
                    "value": "298"
                },
                {
                    "value": "2718"
                },
                {
                    "value": "1194"
                },
                {
                    "value": "1151"
                },
                {
                    "value": "1576"
                },
                {
                    "value": "279"
                },
                {
                    "value": "269"
                },
                {
                    "value": "128"
                },
                {
                    "value": "11774"
                },
                {
                    "value": "2260"
                },
                {
                    "value": "1678"
                },
                {
                    "value": "3172"
                },
                {
                    "value": "0"
                }
            ]
        },
        {
            "seriesname": "ctgov",
            "data": [
                {
                    "value": "840"
                },
                {
                    "value": "36"
                },
                {
                    "value": "36"
                },
                {
                    "value": "629"
                },
                {
                    "value": "153"
                },
                {
                    "value": "194"
                },
                {
                    "value": "181"
                },
                {
                    "value": "681"
                },
                {
                    "value": "1110"
                },
                {
                    "value": "230"
                },
                {
                    "value": "309"
                },
                {
                    "value": "802"
                },
                {
                    "value": "555"
                }
            ]
        }
   ]

}""")




  return  render(request, 'demo/chart.html', {'output1' : column2d1.render(),
    'output2' : column2d2.render(),'chart':chart1.render(),})
      
  