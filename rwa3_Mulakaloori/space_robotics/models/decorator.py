
def decorator(method : object):
    def wrapper(*args,**kwargs):
        emoji = {
            'add_robot' : '✅',
            'remove_robot' : '❌',
            'activate' : '🔌',
            'deploy_mission' : '🚀',
            'report_status' : '📊',
        }
        print(f"{emoji[method.__name__] * 2}  Executing {method.__name__} method  {emoji[method.__name__] * 2}") 
        return_value = method(*args,**kwargs) 
        return return_value
    return wrapper
        
        
        
        
    