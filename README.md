openshiftwebpy
==============

Running on OpenShift
--------------------

Create an account at http://openshift.redhat.com/

Create a python application

    rhc app create openshiftwebpy python-2.6

Add this upstream openshiftwebpy repo

    cd openshiftwebpy
    git remote add upstream -m master git://github.com/openshift/openshiftwebpy.git
    git pull -s recursive -X theirs upstream master

Then push the repo upstream

    git push

That's it, you can now checkout your application at:
    http://openshiftwebpy-$yournamespace.rhcloud.com


