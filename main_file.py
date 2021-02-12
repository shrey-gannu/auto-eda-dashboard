def complete_function(df1):
  import pandas as pd
  import numpy as np
  import summary as sm
  from matplotlib import pyplot as plt
  import ipywidgets as widgets
  from ipywidgets import HBox, VBox
  from IPython.display import display
  import visualisation as vz

  # dividing variables into categorical and continuous
  categorical = []                      # All columns which are categorical in nature
  numerical = []                        # All features that are continous in nature
  for x in df1.columns:
      if np.unique(df1[x].astype('str')).size <= 0.1*len(df1.index):
          categorical.append(x)
      else:
          numerical.append(x)

# all output widgets initiallised

  dataset_sum = widgets.Output()
  var_sum = widgets.Output()
  graphVar1 = widgets.Output()
  graphVar2 = widgets.Output()
  graphVar3 = widgets.Output()

  # all dropdown menus in the dash defined
  var1 = widgets.Dropdown(options =(df1.columns).tolist())
  var_1 = widgets.Dropdown(options =(df1.columns).tolist())
  var_2 = widgets.Dropdown(options =(df1.columns).tolist())
  var__1 = widgets.Dropdown(options =(df1.columns).tolist())
  var__2 = widgets.Dropdown(options =(df1.columns).tolist())
  var__3 = widgets.Dropdown(options =(df1.columns).tolist())

# tab 2 displays summary of variable and a graph of the variable
  def TAB2(var1_change):
      graphVar1.clear_output()
      with var_sum:
          var_sum.clear_output()
          if var1_change in categorical:
              temp = sm.catsum(df1,var1_change)
          else:
              temp = sm.numsum(df1,var1_change)
          for key, value in temp.items():
              print(key, ' : ', value)
            
      with graphVar1:
          if var1_change in categorical:
               vz.cat_vis(df1,var1_change)
               plt.show()
          else:
              vz.num_vis(df1,var1_change)
              plt.show()

# tab 3 shows relation between 2 variables

  def TAB3(var_1_change,var_2_change):
      graphVar2.clear_output()
      with graphVar2:
          vz.tab3_vis(df1,var_1_change,var_2_change)
          plt.show()

# tab 4 shows relation between 3 variables, 3rd as a hue
  def TAB4(var__1_change,var__2_change,var__3_change):
    graphVar3.clear_output()
    with graphVar3:
        vz.tab4_viz(df1,var__1_change,var__2_change,var__3_change)
        plt.show()

 # event handlers for al variable dropdowns
  def var1_handler(change):
      TAB2(change.new)
  def var_1_handler(change):
      TAB3(change.new,var_2.value)
  def var_2_handler(change):
      TAB3(var_1.value,change.new)
  def var__1_handler(change):
      TAB4(change.new,var__2.value,var__3.value)
  def var__2_handler(change):
      TAB4(var__1.value,change.new,var__3.value)
  def var__3_handler(change):
      TAB4(var__1.value,var__2.value,change.new)

# observer function for all variable dropdowns
  var1.observe(var1_handler, names = 'value')
  var_1.observe(var_1_handler, names = 'value')
  var_2.observe(var_2_handler, names = 'value')
  var__1.observe(var__1_handler, names = 'value')
  var__2.observe(var__2_handler, names = 'value')
  var__3.observe(var__3_handler, names = 'value')

  tab1 = VBox(children=[dataset_sum])
  tab2 = HBox(children = [VBox(children = [var1,var_sum]),graphVar1] )
  tab3 = HBox(children = [VBox(children = [var_1,var_2]),graphVar2])
  tab4 = HBox(children = [VBox(children = [var__1,var__2,var__3]),graphVar3])
  
  tab = widgets.Tab(children = [tab1,tab2,tab3,tab4])
  tab.set_title(0, 'Dataset summary')
  tab.set_title(1, 'Variable summary')
  tab.set_title(2,'Var1 vs Var2')
  tab.set_title(3,'Var1 vs Var2 vs Var3')
  
  dashboard = widgets.VBox([tab])
  display(dashboard)

  return None



    

      



