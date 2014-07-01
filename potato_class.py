from crop_class import *
class Potato(Crop):
    """A representation of a potato crop"""
    
    def __init__(self):
        #call super class constructor
        super().__init__(2,6,7)
        self._type = "Potato"
        
    def grow (self,light,water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling" and water > self._water_need:
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._growth += self._growth_rate * 1.25
            else:
                self._growth += self._growth_rate
        #increment the days growing
        self._days_growing += 1
        #update the status
        self._update_status()

if __name__ == "__main__":
    potato_crop = Potato()
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
    manual_grow(potato_crop)
    print(potato_crop.report())
