import json
import matplotlib.pyplot as plt

from paprika.io import *

def plot_comparison(json1, label1, json2, label2, method='ti-block'):
    with open(json1) as file:
        results1 = json.load(file, object_hook=json_numpy_obj_hook)
        
    with open(json2) as file:
        results2 = json.load(file, object_hook=json_numpy_obj_hook)
    
    plt.figure(figsize=(16,4.5))
    plt.subplot(1,3,1)
    plt.plot(results1['attach'][method]['fe_matrix'][0,:], 'o-', label=label1)
    plt.plot(results2['attach'][method]['fe_matrix'][0,:], 'o-', label=label2)
    plt.legend()
    plt.xlabel("Attach", fontsize=16)
    plt.ylabel(r"$\Delta$G (kcal/mol)", fontsize=16)
    plt.title(
        f"{label1}: {results1['attach'][method]['fe']:.2f} +- {results1['attach'][method]['sem']:.2f} kcal/mol\n"
        f"{label2}: {results2['attach'][method]['fe']:.2f} +- {results2['attach'][method]['sem']:.2f} kcal/mol"
    )

    plt.subplot(1,3,2)
    plt.plot(results1['pull'][method]['fe_matrix'][0,:], 'o-')
    plt.plot(results2['pull'][method]['fe_matrix'][0,:], 'o-')
    plt.xlabel("Pull", fontsize=16)
    plt.title(
        f"{label1}: {results1['pull'][method]['fe']:.2f} +- {results1['pull'][method]['sem']:.2f} kcal/mol\n"
        f"{label2}: {results2['pull'][method]['fe']:.2f} +- {results2['pull'][method]['sem']:.2f} kcal/mol"
    )

    plt.subplot(1,3,3)
    plt.plot(results1['release'][method]['fe_matrix'][0,:], 'o-')
    plt.plot(results2['release'][method]['fe_matrix'][0,:], 'o-')
    plt.xlabel("Release", fontsize=16)
    plt.title(
        f"{label1}: {results1['release'][method]['fe']:.2f} +- {results1['release'][method]['sem']:.2f} kcal/mol\n"
        f"{label2}: {results2['release'][method]['fe']:.2f} +- {results2['release'][method]['sem']:.2f} kcal/mol"
    )
    
    
    restraint1 = results1['attach'][method]['fe'] - results1['release'][method]['fe'] + results1['ref_state_work']
    restraint2 = results2['attach'][method]['fe'] - results2['release'][method]['fe'] + results2['ref_state_work']
    
    barrier1 = np.max(results1['pull'][method]['fe_matrix'][0,:]) - np.min(results1['pull'][method]['fe_matrix'][0,:])
    barrier2 = np.max(results2['pull'][method]['fe_matrix'][0,:]) - np.min(results2['pull'][method]['fe_matrix'][0,:])