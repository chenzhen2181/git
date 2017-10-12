# encoding:UTF-8

def savefile(filename,html,useagent):
    with open(filename, 'a') as f:
        f.write("%s\n\n" %useagent )
        f.writelines(html.read())



