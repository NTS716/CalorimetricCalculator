def main():

        #get inputs and convert them to floats
        def getMass():
                global mass
                mass_inp = raw_input("\nEnter Mass: ")
                try:
                        mass = float(mass_inp)
                except ValueError:
                        print "\nnot a number\n"
                        getMass()

        def getInitHeat():
                global initHeat
                initHeat_inp = raw_input("\nEnter Initial Heat: ")
                try:
                        initHeat = float(initHeat_inp)
                except ValueError:
                        print "\nnot a number\n"
                        getInitHeat()

        def getFinalHeat():
                global finalHeat
                finalHeat_inp = raw_input("\nEnter Final Heat: ")
                try:
                        finalHeat = float(finalHeat_inp)
                except ValueError:
                        print "\nnot a number\n"
                        getFinalHeat()

        def getSpecifHeat():
                global specifHeat
                specifHeat_inp = raw_input("\nEnter Specific Heat: ")
                try:
                        specifHeat = float(specifHeat_inp)
                except ValueError:
                        print "\nnot a number\n"
                        getSpecifHeat()

        # define a function that runs all of the input function 
        def getInputs():
                getMass()
                getInitHeat()
                getFinalHeat()
                getSpecifHeat()

        # run the getInputs function
        getInputs()

        # get answer and write to file
        q = (mass * specifHeat * (finalHeat - initHeat))
        output = open('Answer.txt', "a")
        output.truncate()
        output.write(str(q))
        
if __name__ == '__main__':
        main()
