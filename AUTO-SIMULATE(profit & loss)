# Skeleton Program for the AQA AS Summer 2024 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in a Python 3 environment

# Version number: 0.0.1

BLANK = "   "
MAX_Q_SIZE = 30
MAX_TILLS = 5
MAX_TIME = 50
TILL_SPEED = 3

TIME_IDLE = 0
TIME_BUSY = 1
TIME_SERVING = 2

ARRIVAL_TIME = 0
ITEMS = 1

# indices for Stats data structure
MAX_Q_LENGTH = 0
MAX_WAIT = 1
TOTAL_WAIT = 2
TOTAL_Q = 3
TOTAL_Q_OCCURRENCE = 4
TOTAL_NO_WAIT = 5
PROFIT = 6
WORKNIG_TIME = 7

# costs
ITEM_COST = 1
TILL_COST = 0.2

class Q_Node:
  def __init__(self):
    self.BuyerID = BLANK
    self.WaitingTime = 0
    self.ItemsInBasket = 0

def ResetDataStructures():
  Stats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  Tills = [[0, 0, 0] for i in range(MAX_TILLS + 1)]
  BuyerQ = [Q_Node() for i in range(MAX_Q_SIZE)]
  return Stats, Tills, BuyerQ

def ChangeSettings():
  SimulationTime = 10
  NoOfTills = 2
  print("Settings set for this simulation:")
  print("=================================")
  print(f"Simulation time: {SimulationTime}")
  print(f"Tills operating: {NoOfTills}")
  print("=================================")
  print()
  Answer = input("Do you wish to change the settings?  Y/N: ")
  if Answer == 'Y':
    print(f"Maximum simulation time is {MAX_TIME} time units")
    SimulationTime = int(input("Simulation run time: "))
    while SimulationTime > MAX_TIME or SimulationTime < 1:
      print(f"Maximum simulation time is {MAX_TIME} time units")
      SimulationTime = int(input("Simulation run time: "))
    print(f"Maximum number of tills is {MAX_TILLS}")
    NoOfTills = int(input("Number of tills in use: "))
    while NoOfTills > MAX_TILLS or NoOfTills < 1:
      print(f"Maximum number of tills is {MAX_TILLS}")
      NoOfTills = int(input("Number of tills in use: "))
  return SimulationTime, NoOfTills

def ReadInSimulationData():
  Data = [[0, 0] for i in range(MAX_TIME + 1)]
  FileIn = open("SimulationData.txt", 'r')
  DataString = FileIn.readline()
  Count = 0
  while DataString != "" and Count < MAX_TIME:
    Count += 1
    Data[Count][ARRIVAL_TIME] = int(DataString[0])
    Data[Count][ITEMS] = int(DataString[2:])
    DataString = FileIn.readline()
  FileIn.close()
  return Data

def OutputHeading():
  print()
  print("Time Buyer  | Start Till Serve | Till Time Time Time |      Queue")
  print("     enters | serve      time  | num- idle busy ser- | Buyer Wait Items")
  print("     (items)| buyer            | ber            ving | ID    time in")
  print("            |                  |                     |            basket")
 
def BuyerJoinsQ(Data, BuyerQ, QLength, BuyerNumber):
  ItemsInBasket = Data[BuyerNumber][ITEMS]
  BuyerQ[QLength].BuyerID = f"B{BuyerNumber}"
  BuyerQ[QLength].ItemsInBasket  = ItemsInBasket
  QLength += 1
  return BuyerQ, QLength

def BuyerArrives(Data, BuyerQ, QLength, BuyerNumber, NoOfTills, Stats, Sale):
  # print(f"  B{BuyerNumber}({Data[BuyerNumber][ITEMS]})")
  BuyerQ, QLength = BuyerJoinsQ(Data, BuyerQ, QLength, BuyerNumber)
  Sale += Data[BuyerNumber][ITEMS] * ITEM_COST
  return BuyerQ, QLength, NoOfTills, Stats, Sale

def FindFreeTill(Tills, NoOfTills):
  FoundFreeTill = False
  TillNumber = 0
  while not FoundFreeTill and TillNumber < NoOfTills:
    TillNumber += 1
    if Tills[TillNumber][TIME_SERVING] == 0:
      FoundFreeTill = True
  if FoundFreeTill:
    return TillNumber
  else:
    return -1

def ServeBuyer(BuyerQ, QLength):
  ThisBuyerID = BuyerQ[0].BuyerID
  ThisBuyerWaitingTime = BuyerQ[0].WaitingTime
  ThisBuyerItems = BuyerQ[0].ItemsInBasket
  for Count in range(QLength):
    BuyerQ[Count].BuyerID = BuyerQ[Count + 1].BuyerID
    BuyerQ[Count].WaitingTime = BuyerQ[Count + 1].WaitingTime
    BuyerQ[Count].ItemsInBasket = BuyerQ[Count + 1].ItemsInBasket
  BuyerQ[QLength].BuyerID = BLANK
  BuyerQ[QLength].WaitingTime = 0
  BuyerQ[QLength].ItemsInBasket = 0
  QLength -= 1
  # print(f"{ThisBuyerID:>17s}", end='')
  return BuyerQ, QLength, ThisBuyerID, ThisBuyerWaitingTime, ThisBuyerItems

def UpdateStats(Stats, WaitingTime):
  Stats[TOTAL_WAIT] += WaitingTime
  if WaitingTime > Stats[MAX_WAIT]:
    Stats[MAX_WAIT] = WaitingTime
  if WaitingTime == 0:
    Stats[TOTAL_NO_WAIT] += 1
  return Stats

def CalculateServingTime(Tills, ThisTill, NoOfItems):
  ServingTime = (NoOfItems // TILL_SPEED) + 1
  Tills[ThisTill][TIME_SERVING] = ServingTime
  # print(f"{ThisTill:>6d}{ServingTime:>6d}")
  return Tills

def IncrementTimeWaiting(BuyerQ, QLength):
  for Count in range(QLength):
    BuyerQ[Count].WaitingTime += 1
  return BuyerQ

def UpdateTills(Tills, NoOfTills):
  for TillNumber in range(NoOfTills + 1):
    if Tills[TillNumber][TIME_SERVING] == 0:
      Tills[TillNumber][TIME_IDLE] += 1
    else:
      Tills[TillNumber][TIME_BUSY] += 1
      Tills[TillNumber][TIME_SERVING] -= 1
  return Tills

def OutputTillAndQueueStates(Tills, NoOfTills, BuyerQ, QLength):
  for i in range(1, NoOfTills + 1):
    print(f"{i:>36d}{Tills[i][TIME_IDLE]:>5d}{Tills[i][TIME_BUSY]:>5d}{Tills[i][TIME_SERVING]:>6d}")
  print("                                                    ** Start of queue **")
  for i in range(QLength):
    print(f"{BuyerQ[i].BuyerID:>57s}{BuyerQ[i].WaitingTime:>7d}{BuyerQ[i].ItemsInBasket:>6d}")
  print("                                                    *** End of queue ***")
  print("------------------------------------------------------------------------")

def Serving(Tills, NoOfTills, BuyerQ, QLength, Stats):
  TillFree = FindFreeTill(Tills, NoOfTills)
  while TillFree != -1 and QLength > 0:
    BuyerQ, QLength, BuyerID, WaitingTime, ItemsInBasket = ServeBuyer(BuyerQ, QLength)
    Stats = UpdateStats(Stats, WaitingTime)
    Tills = CalculateServingTime(Tills, TillFree, ItemsInBasket)
    TillFree = FindFreeTill(Tills, NoOfTills)
  BuyerQ = IncrementTimeWaiting(BuyerQ, QLength)
  Tills = UpdateTills(Tills, NoOfTills)
  if QLength > 0:
    Stats[TOTAL_Q_OCCURRENCE] += 1 
    Stats[TOTAL_Q] += QLength 
  if QLength > Stats[MAX_Q_LENGTH]:
    Stats[MAX_Q_LENGTH] = QLength 
  # OutputTillAndQueueStates(Tills, NoOfTills, BuyerQ, QLength)
  return  Tills, NoOfTills, BuyerQ, QLength, Stats

def TillsBusy(Tills, NoOfTills):
  IsBusy = False
  TillNumber = 0
  while not IsBusy and TillNumber <= NoOfTills:
    if Tills[TillNumber][TIME_SERVING] > 0:
      IsBusy = True
    TillNumber += 1
  return IsBusy

def OutputStats(Stats, BuyerNumber, SimulationTime, Tills, NoOfTills):
  Total_time_working = 0  #🟢
  for x in range(1, NoOfTills + 1): #🟢
    Total_time_working += Tills[x][TIME_BUSY] #🟢
    Total_time_working += Tills[x][TIME_IDLE] #🟢 finds total number of time for which till is ON.
    # used to find the total number of time units all tills cumulatively worked!
  # print("The simulation statistics are:")
  # print("==============================")
  # print(f"The maximum queue length was: {Stats[MAX_Q_LENGTH]} buyers")
  # print(f"The maximum waiting time was: {Stats[MAX_WAIT]} time units")
  # print(f"{BuyerNumber} buyers arrived during {SimulationTime} time units")
  # AverageWaitingTime = round(Stats[TOTAL_WAIT] / BuyerNumber, 1)
  # print(f"The average waiting time was: {AverageWaitingTime} time units")
  print(f"😊 Profit: {Stats[PROFIT] - (0.2 * Total_time_working)}") #🟢 # times it by 0.2 and subtract by money made selling all items
  if Stats[TOTAL_Q_OCCURRENCE] > 0:
    AverageQLength = round(Stats[TOTAL_Q] / Stats[TOTAL_Q_OCCURRENCE], 2)
    print(f"The average queue length was: {AverageQLength} buyers")
  else: 
    print("No queue length")
  print()
  # print(f"{Stats[TOTAL_NO_WAIT]} buyers did not need to queue")

def QueueSimulator(SimulationTime, NoOfTills):
  BuyerNumber = 0
  QLength = 0
  Sale = 0
  Working_Time = 0
  Stats, Tills, BuyerQ = ResetDataStructures()
  # SimulationTime, NoOfTills = ChangeSettings()
  Data = ReadInSimulationData()
  # OutputHeading()
  TimeToNextArrival = Data[BuyerNumber + 1][ARRIVAL_TIME]
  for TimeUnit in range(SimulationTime):
    TimeToNextArrival -= 1
    # print(f"{TimeUnit:>3d}", end='')
    if TimeToNextArrival == 0:
      BuyerNumber += 1
      BuyerQ, QLength, NoOfTills, Stats, Sale = BuyerArrives(Data, BuyerQ, QLength, BuyerNumber, NoOfTills, Stats, Sale)
      TimeToNextArrival = Data[BuyerNumber + 1][ARRIVAL_TIME]
    else:
      pass
      # print()
    Tills, NoOfTills, BuyerQ, QLength, Stats = Serving(Tills, NoOfTills, BuyerQ, QLength, Stats)
  Stats[PROFIT] = Sale
  ExtraTime = 0  # note: in extra times, no new people join the queue. Hence, we don't need to incoorperate a function which adds number of items buyer buys.
  while QLength > 0:
    TimeUnit = SimulationTime + ExtraTime
    # print(f"{TimeUnit:>3d}")
    Tills, NoOfTills, BuyerQ, QLength, Stats = Serving(Tills, NoOfTills, BuyerQ, QLength, Stats)
    ExtraTime += 1
  while TillsBusy(Tills, NoOfTills):
    TimeUnit = SimulationTime + ExtraTime
    # print(f"{TimeUnit:>3d}")
    Tills = UpdateTills(Tills, NoOfTills)
    # OutputTillAndQueueStates(Tills, NoOfTills, BuyerQ, QLength)
    ExtraTime += 1
  OutputStats(Stats, BuyerNumber, SimulationTime, Tills, NoOfTills)

if __name__ == "__main__":
  for Time in range(1,51):
    for Tills in range(1,6):
      # print("##########")
      print(f"time: {Time} tills: {Tills}")
      # print("##########")
      QueueSimulator(Time, Tills)  # this works. but ends up printing long list of all simulations.
  input("Press Enter to finish")
  # we want a way for this queue simulator to run incrementing each time it's simulation time and number of tills.
  # we can do this by passing in parameters of SimulationTime and NoOfTills
  # clearly we can see that the "best" number of tills is 5 number of tills.
  # however, it gets interesting when there is profit and loss.
