install flask


in this directory, run like


$ export FLASK_APP=proposalMgt/operations.py


and


$ python -m flask run


then send requst like


GET http://localhost:5000/getProposalById/id=1
