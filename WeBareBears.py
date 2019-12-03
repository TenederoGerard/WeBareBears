import pandas as pd

Math = {'Student': ['Ice Bear','Panda', 'Grizzly'], 'Math': [80,95,79]}
Electronic = {'Student':['Ice Bear','Panda', 'Grizzly'],'Electronics': [85,81,83]}
Gea = {'Student':['Ice Bear','Panda', 'Grizzly'], 'Geas': [90,79,93]}
Esat = {'Student':['Ice Bear','Panda', 'Grizzly'], 'Esat': [93,89,88]}

Maths = pd.DataFrame (Math, columns = ['Student','Math'])
Electronics = pd.DataFrame (Electronic, columns = ['Student','Electronics'])
Geas = pd.DataFrame (Gea, columns = ['Student', 'Geas'])
Esats = pd.DataFrame (Esat, columns = ['Student','Esat'])

Combi_Bears = pd.merge (Maths,Electronics)
Combo_Bears = pd.merge (Combi_Bears, Geas)
Super_Bears = pd.merge (Combo_Bears,Esats)

tidy_bears = pd.melt (Super_Bears, id_vars= 'Student', value_vars = ['Math', 'Electronics', 'Geas','Esat'])
b = tidy_bears.rename (columns = {'variable' : 'Subject', 'value' : 'Grades'})
c = b.sort_values ('Student')
d = c.reset_index()
e = d.drop (columns = ['index'])
