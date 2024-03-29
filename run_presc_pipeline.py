### Import all the necessary Modules
import get_all_variables as gav
from create_objects import get_spark_object
from validations import get_curr_date
import sys



def main():
    try:
        ### Get Spark Object
        spark = get_spark_object(gav.envn,gav.appName)
        # Validate Spark Object
        get_curr_date(spark)
        ### Initiate run_presc_data_ingest Script
        # Load the City File
        # Load the Prescriber Fact File
        # Validate
        # Set up Error Handling
        # Set up Logging Configuration Mechanism
        ### Initiate run_presc_data_preprocessing Script
        # Set up Logging Configuration Mechanism
        ### Initiate run_presc_data_transform Script
        # Apply all the transfrmations Logics
        # Validate
        # Set up Logging Configuration Mechanism
        ### Initiate run_data_extraction Script
        # Validate
        # Set up Error Handling
        # Set up Logging Configuration Mechanism
    except Exception as exp:
        print("Error Occured in the main() method. Please check the Stack Trace to go to the respective module and fix it." +str(exp))
        sys.exit(1)
### End of Application Part 1
# check whether the current script is being run as the main program or whether it is being imported as a module into another program.
if __name__ == "__main__" :
    main()