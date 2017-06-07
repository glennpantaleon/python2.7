def Q_and_A():
    '''The purpose of this program is to answer questions about the CS 1114 course.'''

def main():
    import os
    print'''
    *Professor's Information:
    Q: What's your lecture professor's name?
    A: The professor's name is Evan Gallagher.
    Q: What are his office hours?
    A: Professor Gallagher is available on:
    Mondays             Wednesdays                      Tuesdays and Thursdays
    2:15-2:45 pm        1:00-2:45 pm ; 6:15-8:15 pm     3:30-4:00 pm and after 5:30 pm

    Q: Where is his office?
    A: Professor Gallagher's office is located in Dibner Library in room LC117.
    '''
    print'''
    *Exam Locations and Times
    Q: What is the date and time of the first and second tests?
    A: The date and time of these exams are on:
    First Exam                      Second Exam                 
    March 5 2012                    April 9 2012                
    1:30-3:00 pm                    1:30-3:00 pm                
    During Common Exam Period       During Common Exam Period
    
    Q: What is the period during which final exams are given?
    A: The period for the final exam is to be annoucned.
    '''
    os.system("pause")
# are we being executed?
if __name__== '__main__':  
    main()
    
