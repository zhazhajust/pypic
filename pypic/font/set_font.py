from matplotlib import rcParams

########################################
############# Default Font #############
########################################

font_params = {#'font.family':'serif',
        'figure.figsize': (4, 3),
        'font.family':'Times New Roman',
        #'font.style':'italic',
        'mathtext.fontset':'stix',
        'font.weight':'normal', #or 'blod'
        'font.size':16,#or large,small
        }

########################################
########################################
########################################

def setFont(params = font_params):
    rcParams.update(params)