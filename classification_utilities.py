import numpy as np

def display_cm(cm, labels, hide_zeros=False,
                             display_metrics=False):
    """Display confusion matrix with labels, along with
       metrics such as Recall, Precision and F1 score.
       Based on Zach Guo's print_cm gist at
       https://gist.github.com/zachguo/10296432
    """
    precision = np.diagonal(cm)/cm.sum(axis=0).astype('float')
    recall = np.diagonal(cm)/cm.sum(axis=1).astype('float')
    F1 = 2 * (precision * recall) / (precision + recall)
    
    precision[np.isnan(precision)] = 0
    recall[np.isnan(recall)] = 0
    F1[np.isnan(F1)] = 0
    
    total_precision = np.sum(precision * cm.sum(axis=1)) / cm.sum(axis=(0,1))
    total_recall = np.sum(recall * cm.sum(axis=1)) / cm.sum(axis=(0,1))
    total_F1 = np.sum(F1 * cm.sum(axis=1)) / cm.sum(axis=(0,1))
    #print total_precision
    
    #columnwidth = max([len(x) for x in labels]+[5]) # 5 is value length
    columnwidth = max([len(x) for x in labels]+[6]) # 5 is value length
    
    empty_cell = " " * columnwidth
    
    print()
    # Print header
    print( "    " + " Pred >", end=" ")  ,
    for label in labels: 
        print( "%{0}s".format(columnwidth) % label, end=" ") ,
    print( "%{0}s".format(columnwidth) % 'Total', end=" ")
    print()
    print( "    " + " True")
    # Print rows
    for i, label1 in enumerate(labels):
        print( "    %{0}s".format(columnwidth) % label1, end=" ") ,
        for j in range(len(labels)): 
            cell = "%{0}d".format(columnwidth) % cm[i, j]
            if hide_zeros:
                cell = cell if float(cm[i, j]) != 0 else empty_cell
            print( cell, end=" ") ,
        print( "%{0}d".format(columnwidth) % sum(cm[i,:]), end=" ")
        
        print()
        
    if display_metrics:
        print()
        print( "Precision", end=" ") ,
        for j in range(len(labels)):
            cell = "%{0}.2f".format(columnwidth) % precision[j]
            print( cell, end=" " ) ,
        print( "%{0}.2f".format(columnwidth) % total_precision, end=" ")
        print()
        print( "   Recall", end=" ") ,
        for j in range(len(labels)):
            cell = "%{0}.2f".format(columnwidth) % recall[j]
            print( cell, end=" ") ,
        print( "%{0}.2f".format(columnwidth) % total_recall, end=" ")
        print()
        print( "       F1", end=" ") ,
        for j in range(len(labels)):
            cell = "%{0}.2f".format(columnwidth) % F1[j]
            print( cell, end=" ") ,
        print( "%{0}.2f".format(columnwidth) % total_F1, end=" ")
        print()





#def print_cm(cm, labels, hide_zeroes=False, hide_diagonal=False, hide_threshold=None):
#    """pretty print for confusion matrixes"""
#    columnwidth = max([len(x) for x in labels] + [5])  # 5 is value length
#    empty_cell = " " * columnwidth
#    # Print header
#    print("    " + empty_cell, end=" ")
#    for label in labels:
#        print("%{0}s".format(columnwidth) % label, end=" ")
#    print()
#    # Print rows
#    for i, label1 in enumerate(labels):
#        print("    %{0}s".format(columnwidth) % label1, end=" ")
#        for j in range(len(labels)):
#            cell = "%{0}.1f".format(columnwidth) % cm[i, j]
#            if hide_zeroes:
#                cell = cell if float(cm[i, j]) != 0 else empty_cell
#            if hide_diagonal:
#                cell = cell if i != j else empty_cell
#            if hide_threshold:
#                cell = cell if cm[i, j] > hide_threshold else empty_cell
#            print(cell, end=" ")
#        print()







    
                  
def display_adj_cm(
        cm, labels, adjacent_facies, hide_zeros=False, 
        display_metrics=False):
    """This function displays a confusion matrix that counts 
       adjacent facies as correct.
    """
    adj_cm = np.copy(cm)
    
    for i in np.arange(0,cm.shape[0]):
        for j in adjacent_facies[i]:
            adj_cm[i][i] += adj_cm[i][j]
            adj_cm[i][j] = 0.0
        
    display_cm(adj_cm, labels, hide_zeros, 
                             display_metrics)
        