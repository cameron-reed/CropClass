from crop_class import *
class Wheat(Crop):
    """A representation of a wheat crop"""
    
    def __init__(self):
        #call super class constructor
        super().__init__(1,3,6)
        self._type = "Wheat"
        
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
    wheat_crop = Wheat()
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
    manual_grow(wheat_crop)
    print(wheat_crop.report())
