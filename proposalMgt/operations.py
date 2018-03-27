import services

from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)    
    

@app.route('/getProposalById/id=<int:id>', methods=['GET'])
def getProposalById(id):
    '''
    GET proposal by proposal id
    '''
    if request.method == 'GET' and id > 0:
        return make_response(services.getProposalByIdFromProposalTable(id))


@app.route('/getAllProposals', methods=['GET'])
def getAllProposals():
    '''
    GET all proposals
    '''
    if request.method == 'GET':
        return make_response(services.getAllProposalsFromProposalTable())


@app.route('/getProposalsInStage/stage=<int:stage>', methods=['GET'])
def getProposalsInStage(stage):
    '''
    GET proposals in stage
    '''
    if request.method == 'GET':
        return make_response(services.getProposalsInStageFromProposalAndStageTable(stage))


@app.route('/getProposalsInDistrict/district=<int:district>', methods=['GET'])
def getProposalsInDistrict(district):
    '''
    GET proposals in district
    '''
    if request.method == 'GET':
        return make_response(services.getProposalsInDistrictFromProposalTable(district))


@app.route('/getProposalsSearchIdeaByKeyword/keyword=<string:keyword>', methods=['GET'])
def getProposalsSearchIdeaByKeyword(keyword):
    '''
    GET proposals search idea by keyword
    '''
    if request.method == 'GET':
        return make_response(services.getProposalsSearchIdeaByKeywordFromProposalTable(keyword))


@app.route('/getProposalsSearchNeedByKeyword/keyword=<string:keyword>', methods=['GET'])
def getProposalsSearchNeedByKeyword(keyword):
    '''
    GET proposals search need by keyword
    '''
    if request.method == 'GET':
        return make_response(services.getProposalsSearchNeedByKeywordFromProposalTable(keyword))


@app.route('/getProposalsGlobalSearchByKeyword/keyword=<string:keyword>', methods=['GET'])
def getProposalsGlobalSearchByKeyword(keyword):
    '''
    GET proposals global search by keyword
    '''
    if request.method == 'GET':
        return make_response(services.getProposalsGlobalSearchByKeywordFromProposalTable(keyword))
    

@app.route('/updateProposalById/id=<int:id>', methods=['POST'])
def updateProposalById(id):
    '''
    POST edited proposal by id
    '''
    if request.method == 'POST' and validProposal(request.form):
        editedProposal = {
            "id": request.form['id'],
            "status": request.form['status'],
            "idea": request.form['idea'],
            "location": request.form['location'],
            "need": request.form['need'],
            "benefit": request.form['benefit'],
            "district": request.form['district'],
            "angency": request.form['agency'],
            "longitude": request.form['longitude'],
            "latitude": request.form['latitude'],
            "cate": request.form['cate'],
            "comments": request.form['comments']
        }
        return make_response(services.updateProposalByIdToProposalTable(id, editedProposal))