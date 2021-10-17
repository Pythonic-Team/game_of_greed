class Banker:
  
  def __init__(self, shelved = 0):
        self.shelved = shelved

  def shelf(self, num):
    
    """
        Will temporarily store unbanked points
        Argument:
        is the amount of points (integer) to add to shelf.          
    """
    self.shelved +=num
    return self.shelved

list1 = Banker()
print(list1.shelf(20))
print(list1.shelf(40))