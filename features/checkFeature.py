import sys
sys.path.append('modules')
import modulePkg
if (modulePkg.date.get_hour()>15):
    print("Good Afternoon yaaar")
elif(modulePkg.date.get_hour()<15):
    print("Arey its morning")