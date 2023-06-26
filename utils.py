def print_score(true, pred):
    from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, classification_report

    print('<Accuracy Score>')
    print(accuracy_score(true, pred))
    print('<F1-Score>')
    print(f1_score(true, pred))
    print('<Roc-Auc Score>')
    print(roc_auc_score(true, pred))
    print(classification_report(true, pred))
    print()