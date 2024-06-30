import win32com.client
import time
import shutil

app = win32com.client.Dispatch("CANoe.Application")
print(app.UI.Write.Text)
sFilePath = 'C:\\Users\\Anush\\OneDrive\\Dokumente\\_2_Coding\\Python\\Testing\\CANoe\\writeWindowOutput.txt'
sConfigPath = 'C:\\Users\\Anush\\OneDrive\\Dokumente\\_2_Coding\\Python\\Testing\\CANoe\\Easy_WriteWindow.cfg'
app.Open(sConfigPath)
app.Measurement.Start()
time.sleep(100)
#app.UI.Write.EnableOutputFile(sFilePath)
app.Measurement.Stop()
dst = "C:\\Users\\Anush\\CANoe_WriteWindow\\writewindow_1.txt"
shutil.copy(sFilePath, dst)
#app.UI.Write.DisableOutputFile()

app.Measurement.Start()
time.sleep(100)
app.Measurement.Stop()
dst = "C:\\Users\\Anush\\CANoe_WriteWindow\\writewindow_2.txt"
shutil.copyfile(sFilePath, dst)
