hourly_temp = [40.0, 39.0, 37.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               40.0, 41.0, 44.0, 45.0, 47.0, 48.0, 45.0, 42.0, 39.0, 37.0, \
               36.0, 35.0, 33.0, 32.0]
hourlyb_temp = [42.0, 33.0, 34.0, 34.0, 33.0, 34.0, 36.0, 37.0, 38.0, 39.0, \
               42.0, 41.0, 44.0, 45.0, 47.0, 50.0, 45.0, 42.0, 49.0, 40.0, \
               20.0, 33.0, 34.0, 31.0]

def problem2_8(temp_list):
    
    a = 0
    maxtemp = max(temp_list)
    mintemp = min(temp_list)
    
    for i in range(len(temp_list)):
        a = a + temp_list[i]
                
    a = a / len(temp_list)
        
    print("Average: ",a)
    print("High: ",maxtemp)
    print("Low: ",mintemp)    
    