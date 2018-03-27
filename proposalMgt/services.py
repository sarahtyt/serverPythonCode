import json
from dbconnection import execute

PROPOSAL_COLUMNS = ['id', 'title', 'idea', 'location', 'cost', 'need', 'latitude', 'longitude', 'type', 'department', 
'benefit', 'district', 'neighborhood']

def updateProposalByIdToProposalTable(id, editedProposal):
    ss = json.dumps(editedProposal)
    return "update Proposal %d, %s" %(id, ss)


def getProposalByIdFromProposalTable(id):
    sql = "SELECT * FROM proposal.proposal_final WHERE proposal_id = %d" %id
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def getAllProposalsFromProposalTable():
    sql = "SELECT * FROM proposal.proposal_final"
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def getProposalsInStageFromProposalAndStageTable(stage):
    stageTableName = "stage.stage%d" %stage
    sql = "SELECT * FROM proposal.proposal_final join %s on proposal.proposal_final.proposal_id = %s.proposal_id" %(stageTableName, stageTableName)
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def getProposalsInDistrictFromProposalTable(district):
    sql = "SELECT * FROM proposal.proposal_final WHERE council_district = %d" %district
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def getProposalsSearchIdeaByKeywordFromProposalTable(keyword):
    sql = "SELECT * FROM proposal.proposal_final WHERE final_proposal_idea LIKE '%" + keyword + "%'"
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def getProposalsSearchNeedByKeywordFromProposalTable(keyword):
    sql = "SELECT * FROM proposal.proposal_final WHERE proposal_need LIKE '%" + keyword + "%'"
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def getProposalsGlobalSearchByKeywordFromProposalTable(keyword):
    sql = "SELECT * FROM proposal.proposal_final WHERE proposal_id LIKE '%" + keyword + "%'" + " OR final_proposal_title LIKE '%" + keyword + "%'" + " OR final_proposal_idea LIKE '%" + keyword + "%'" + " OR final_project_location LIKE '%" + keyword + "%'" + " OR cost LIKE '%" + keyword + "%'" + " OR proposal_need LIKE '%" + keyword + "%'" + " OR final_proposal_latitude LIKE '%" + keyword + "%'" + " OR final_proposal_longitude LIKE '%" + keyword + "%'" + " OR project_type LIKE '%" + keyword + "%'"  + " OR department LIKE '%" + keyword + "%'" + " OR who_benefits LIKE '%" + keyword + "%'" + " OR council_district LIKE '%" + keyword + "%'" + " OR neihborhood LIKE '%" + keyword + "%'" 
    rows = execute(sql)
    results = []
    for row in rows:
        results.append(toProposalObject(row))
    return json.dumps(results)


def toProposalObject(row):
    proposal = {
        "id": int(row[0]),
        "title": str(row[1]),
        "idea": str(row[2]),
        "location": str(row[3]),
        "cost": int(row[4]),
        "need": str(row[5]),
        "latitude": float(row[6]),
        "longitude":float(row[7]),
        "type":str(row[8]),
        "department": str(row[9]),
        "benefit":str(row[10]),
        "district":str(row[11]),
        "neighborhood": str(row[12]),
    }
    return proposal
