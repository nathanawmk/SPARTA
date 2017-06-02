# *****************************************************************
#  Copyright 2013 MIT Lincoln Laboratory  
#  Project:            SPAR
#  Authors:            SY
#  Description:        Constants for TA1 analytics.
#                      
# 
#  Modifications:
#  Date          Name           Modification
#  ----          ----           ------------
#  Earlier       NH             Original Version
#  16 May 2013   SY
#  6 June 2013   MZ             Schema update
#  3 Aug 2013    SY             Another schema update
# *****************************************************************

# SPAR imports:
import spar_python.common.enum as enum
from spar_python.report_generation.common.results_schema import *

### FOR STORING RESULTS IN A DB ###
PARAM_TABLENAME = "key_parameters"
PARAM_TESTNAME = "testname"
PARAM_PID = "param_id"
PARAM_K = "k"
PARAM_D = "d"
PARAM_L = "l"
    
PARAM_FIELDS_TO_TYPES = {
    PARAM_TESTNAME: FIELD_TYPES.TEXT,
    PARAM_PID: FIELD_TYPES.INTEGER,
    PARAM_K: FIELD_TYPES.INTEGER,
    PARAM_D: FIELD_TYPES.INTEGER,
    PARAM_L: FIELD_TYPES.INTEGER}

PARAM_REQUIRED_FIELDS = [
    PARAM_TESTNAME,
    PARAM_PID,
    PARAM_K,
    PARAM_D,
    PARAM_L]

CIRCUIT_TABLENAME = "circuits"
CIRCUIT_TESTNAME = "testname"
CIRCUIT_CID = "circuit_id"
CIRCUIT_W = "w"
CIRCUIT_PID = "param_id"
CIRCUIT_NUMADDS = "num_adds"
CIRCUIT_NUMADDCONSTS = "num_add_consts"
CIRCUIT_NUMMULS = "num_muls"
CIRCUIT_NUMMULCONSTS = "num_mul_consts"
CIRCUIT_NUMROTATES = "num_rotates"
CIRCUIT_NUMSELECTS = "num_selects"
CIRCUIT_NUMLEVELS = "num_levels"
CIRCUIT_NUMGATES = "num_gates"
CIRCUIT_OUTPUTGATETYPE = "output_gate_type"
CIRCUIT_TESTTYPE = "test_type"

CIRCUIT_FIELDS_TO_TYPES = {
    CIRCUIT_TESTNAME: FIELD_TYPES.TEXT,
    CIRCUIT_CID: FIELD_TYPES.INTEGER,
    CIRCUIT_W: FIELD_TYPES.INTEGER,
    CIRCUIT_PID: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMADDS: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMADDCONSTS: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMMULS: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMMULCONSTS: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMROTATES: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMSELECTS: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMLEVELS: FIELD_TYPES.INTEGER,
    CIRCUIT_NUMGATES: FIELD_TYPES.INTEGER,
    CIRCUIT_OUTPUTGATETYPE: FIELD_TYPES.TEXT,
    CIRCUIT_TESTTYPE: FIELD_TYPES.TEXT}

CIRCUIT_REQUIRED_FIELDS = [
    CIRCUIT_TESTNAME,
    CIRCUIT_CID,
    CIRCUIT_W,
    CIRCUIT_PID,
    CIRCUIT_NUMADDS,
    CIRCUIT_NUMADDCONSTS,
    CIRCUIT_NUMMULS,
    CIRCUIT_NUMMULCONSTS,
    CIRCUIT_NUMROTATES,
    CIRCUIT_NUMSELECTS,
    CIRCUIT_NUMLEVELS,
    CIRCUIT_NUMGATES,
    CIRCUIT_OUTPUTGATETYPE,
    CIRCUIT_TESTTYPE]

INPUT_TABLENAME = "inputs"
INPUT_TESTNAME = "testname"
INPUT_IID = "input_id"
INPUT_CID = "circuit_id"
INPUT_NUMZEROS = "num_zeros"
INPUT_NUMONES = "num_ones"
INPUT_CORRECTOUTPUT = "correct_output"

INPUT_FIELDS_TO_TYPES = {
    INPUT_TESTNAME: FIELD_TYPES.TEXT,
    INPUT_IID: FIELD_TYPES.INTEGER,
    INPUT_CID: FIELD_TYPES.INTEGER,
    INPUT_NUMZEROS: FIELD_TYPES.INTEGER,
    INPUT_NUMONES: FIELD_TYPES.INTEGER,
    INPUT_CORRECTOUTPUT: FIELD_TYPES.TEXT}

INPUT_REQUIRED_FIELDS = [
    INPUT_TESTNAME,
    INPUT_IID,
    INPUT_CID,
    INPUT_NUMZEROS,
    INPUT_NUMONES]

PERKEYGEN_TABLENAME = "performer_keygen"
PERKEYGEN_PERFORMERNAME = "performer_name"
PERKEYGEN_TESTNAME = "testname"
PERKEYGEN_TIMESTAMP = "timestamp"
PERKEYGEN_PID = "param_id"
PERKEYGEN_LATENCY = "latency"
PERKEYGEN_TRANSMITLATENCY = "transmit_latency"
PERKEYGEN_KEYSIZE = "keysize"
PERKEYGEN_STATUS = "status"
PERKEYGEN_RECOVERY = "recovery"

PERKEYGEN_FIELDS_TO_TYPES = {
    PERKEYGEN_PERFORMERNAME: FIELD_TYPES.TEXT,
    PERKEYGEN_TESTNAME: FIELD_TYPES.TEXT,
    PERKEYGEN_TIMESTAMP: FIELD_TYPES.TEXT,
    PERKEYGEN_PID: FIELD_TYPES.INTEGER,
    PERKEYGEN_LATENCY: FIELD_TYPES.REAL,
    PERKEYGEN_TRANSMITLATENCY: FIELD_TYPES.REAL,
    PERKEYGEN_KEYSIZE: FIELD_TYPES.REAL,
    PERKEYGEN_STATUS: FIELD_TYPES.TEXT, # to be manually populated
    PERKEYGEN_RECOVERY: FIELD_TYPES.INTEGER} # to contain recovery flag if
                                             # applicable

PERKEYGEN_REQUIRED_FIELDS = [
    PERKEYGEN_PERFORMERNAME,
    PERKEYGEN_TESTNAME,
    PERKEYGEN_TIMESTAMP,
    PERKEYGEN_PID,
    PERKEYGEN_LATENCY,
    PERKEYGEN_TRANSMITLATENCY,
    PERKEYGEN_KEYSIZE]

PERINGESTION_TABLENAME = "performer_circuit_ingestion"
PERINGESTION_PERFORMERNAME = "performer_name"
PERINGESTION_TESTNAME = "testname"
PERINGESTION_TIMESTAMP = "timestamp"
PERINGESTION_CID = "circuit_id"
PERINGESTION_LATENCY = "latency"
PERINGESTION_TRANSMITLATENCY = "transmit_latency"
PERINGESTION_STATUS = "status"
PERINGESTION_RECOVERY = "recovery"

PERINGESTION_FIELDS_TO_TYPES = {
    PERINGESTION_PERFORMERNAME: FIELD_TYPES.TEXT,
    PERINGESTION_TESTNAME: FIELD_TYPES.TEXT,
    PERINGESTION_TIMESTAMP: FIELD_TYPES.TEXT,
    PERINGESTION_CID: FIELD_TYPES.INTEGER,
    PERINGESTION_LATENCY: FIELD_TYPES.REAL,
    PERINGESTION_TRANSMITLATENCY: FIELD_TYPES.REAL,
    PERINGESTION_STATUS: FIELD_TYPES.TEXT, # to be manually populated
    PERINGESTION_RECOVERY: FIELD_TYPES.INTEGER} # to contain recovery flag if
                                                # applicable

PERINGESTION_REQUIRED_FIELDS = [
    PERINGESTION_PERFORMERNAME,
    PERINGESTION_TESTNAME,
    PERINGESTION_TIMESTAMP,
    PERINGESTION_CID,
    PERINGESTION_LATENCY,
    PERINGESTION_TRANSMITLATENCY]

PEREVALUATION_TABLENAME = "performer_evaluation"
PEREVALUATION_PERFORMERNAME = "performer_name"
PEREVALUATION_TESTNAME = "testname"
PEREVALUATION_TIMESTAMP = "timestamp"
PEREVALUATION_IID = "input_id"
PEREVALUATION_INPUTTRANSMITLATENCY = "input_transmit_latency"
PEREVALUATION_OUTPUTTRANSMITLATENCY = "output_transmit_latency"
PEREVALUATION_ENCRYPTIONLATENCY = "encryption_latency"
PEREVALUATION_EVALUATIONLATENCY = "evaluation_latency"
PEREVALUATION_DECRYPTIONLATENCY = "decryption_latency"
PEREVALUATION_OUTPUT = "output"
PEREVALUATION_OUTPUTSIZE = "encrypted_output_size"
PEREVALUATION_INPUTSIZE = "encrypted_input_size"
PEREVALUATION_CORRECTNESS = "correctness"
PEREVALUATION_STATUS = "status"
PEREVALUATION_RECOVERY = "recovery"

PEREVALUATION_FIELDS_TO_TYPES = {
    PEREVALUATION_PERFORMERNAME: FIELD_TYPES.TEXT,
    PEREVALUATION_TESTNAME: FIELD_TYPES.TEXT,
    PEREVALUATION_TIMESTAMP: FIELD_TYPES.TEXT,
    PEREVALUATION_IID: FIELD_TYPES.INTEGER,
    PEREVALUATION_INPUTTRANSMITLATENCY: FIELD_TYPES.REAL,
    PEREVALUATION_OUTPUTTRANSMITLATENCY: FIELD_TYPES.REAL,
    PEREVALUATION_ENCRYPTIONLATENCY: FIELD_TYPES.REAL,
    PEREVALUATION_EVALUATIONLATENCY: FIELD_TYPES.REAL,
    PEREVALUATION_DECRYPTIONLATENCY: FIELD_TYPES.REAL,
    PEREVALUATION_OUTPUT: FIELD_TYPES.TEXT,
    PEREVALUATION_OUTPUTSIZE: FIELD_TYPES.REAL,
    PEREVALUATION_INPUTSIZE: FIELD_TYPES.REAL,
    PEREVALUATION_CORRECTNESS: FIELD_TYPES.BOOL,
    PEREVALUATION_STATUS: FIELD_TYPES.TEXT, # to be manually populated
    PEREVALUATION_RECOVERY: FIELD_TYPES.INTEGER} # to contain recovery flag if
                                                 # applicable

PEREVALUATION_REQUIRED_FIELDS = [
    PEREVALUATION_PERFORMERNAME,
    PEREVALUATION_TESTNAME,
    PEREVALUATION_TIMESTAMP,
    PEREVALUATION_IID,
    PEREVALUATION_INPUTTRANSMITLATENCY,
    PEREVALUATION_OUTPUTTRANSMITLATENCY,
    PEREVALUATION_ENCRYPTIONLATENCY,
    PEREVALUATION_EVALUATIONLATENCY,
    PEREVALUATION_DECRYPTIONLATENCY,
    PEREVALUATION_OUTPUT,
    PEREVALUATION_OUTPUTSIZE,
    PEREVALUATION_INPUTSIZE]

TABLENAME_TO_FIELDTOTYPE = {
    PARAM_TABLENAME: PARAM_FIELDS_TO_TYPES,
    CIRCUIT_TABLENAME: CIRCUIT_FIELDS_TO_TYPES,
    INPUT_TABLENAME: INPUT_FIELDS_TO_TYPES,
    PERKEYGEN_TABLENAME: PERKEYGEN_FIELDS_TO_TYPES,
    PERINGESTION_TABLENAME: PERINGESTION_FIELDS_TO_TYPES,
    PEREVALUATION_TABLENAME: PEREVALUATION_FIELDS_TO_TYPES}

TABLENAME_TO_REQUIREDFIELDS = {
    PARAM_TABLENAME: PARAM_REQUIRED_FIELDS,
    CIRCUIT_TABLENAME: CIRCUIT_REQUIRED_FIELDS,
    INPUT_TABLENAME: INPUT_REQUIRED_FIELDS,
    PERKEYGEN_TABLENAME: PERKEYGEN_REQUIRED_FIELDS,
    PERINGESTION_TABLENAME: PERINGESTION_REQUIRED_FIELDS,
    PEREVALUATION_TABLENAME: PEREVALUATION_REQUIRED_FIELDS}

# a dictionary mapping each table to auxiliary lines necessary in its
# construction:
TABLENAME_TO_AUX = {
    PARAM_TABLENAME: "UNIQUE (%s)" % PARAM_PID,
    CIRCUIT_TABLENAME: ",".join([
        "UNIQUE (%s)" % CIRCUIT_CID,
        "FOREIGN KEY (%s) REFERENCES %s (%s)" %
        (CIRCUIT_PID, PARAM_TABLENAME, PARAM_PID)]),
    INPUT_TABLENAME: ",".join([
        "UNIQUE (%s)" % INPUT_IID,
        "FOREIGN KEY (%s) REFERENCES %s (%s)" %
        (INPUT_CID, CIRCUIT_TABLENAME, CIRCUIT_CID)]),
    PERKEYGEN_TABLENAME: ",".join([
        "FOREIGN KEY (%s) REFERENCES %s (%s)" %
        (PERKEYGEN_PID, PARAM_TABLENAME, PARAM_PID),
        "UNIQUE (%s, %s)" %
        (PERKEYGEN_PID, PERKEYGEN_TIMESTAMP)]),
    PERINGESTION_TABLENAME: ",".join([
        "FOREIGN KEY (%s) REFERENCES %s (%s)" %
        (PERINGESTION_CID, CIRCUIT_TABLENAME, CIRCUIT_CID),
        "UNIQUE (%s, %s)" %
        (PERINGESTION_CID, PERINGESTION_TIMESTAMP)]),
    PEREVALUATION_TABLENAME: ",".join([
        "FOREIGN KEY (%s) REFERENCES %s (%s)" %
        (PEREVALUATION_IID, INPUT_TABLENAME, INPUT_IID),
        "UNIQUE (%s, %s)" %
        (PEREVALUATION_IID,
         PEREVALUATION_TIMESTAMP)])}

PERFORMER_TABLENAMES = set(
    [PERKEYGEN_TABLENAME, PERINGESTION_TABLENAME,
     PEREVALUATION_TABLENAME])

# a list of the non-performer tables, in order from most to least likely to be
# the primary table.
OTHER_TABLENAMES_HEIRARCHY = [
    PARAM_TABLENAME, CIRCUIT_TABLENAME, INPUT_TABLENAME]

# map of primary table to necessary joins (denoted tuples of the
# form (source_table, source_field, target_table, target_field,
# target_table_alias (None if not applicable))):
TABLENAME_TO_JOINS = {
    PARAM_TABLENAME: [],
    CIRCUIT_TABLENAME: [
        (CIRCUIT_TABLENAME,
         CIRCUIT_PID,
         PARAM_TABLENAME,
         PARAM_PID,
         None)],
    INPUT_TABLENAME: [
        (INPUT_TABLENAME,
         INPUT_CID,
         CIRCUIT_TABLENAME,
         CIRCUIT_CID,
         None),
        (CIRCUIT_TABLENAME,
         CIRCUIT_PID,
         PARAM_TABLENAME,
         PARAM_PID,
         None)],
    PERKEYGEN_TABLENAME: [
        (PERKEYGEN_TABLENAME,
         PERKEYGEN_PID,
         PARAM_TABLENAME,
         PARAM_PID,
         None)],
    PERINGESTION_TABLENAME: [
        (PERINGESTION_TABLENAME,
         PERINGESTION_CID,
         CIRCUIT_TABLENAME,
         CIRCUIT_CID,
         None),
        (CIRCUIT_TABLENAME,
         CIRCUIT_PID,
         PARAM_TABLENAME,
         PARAM_PID,
         None)],
    PEREVALUATION_TABLENAME: [
        (PEREVALUATION_TABLENAME,
         PEREVALUATION_IID,
         INPUT_TABLENAME,
         INPUT_IID,
         None),
        (INPUT_TABLENAME,
         INPUT_CID,
         CIRCUIT_TABLENAME,
         CIRCUIT_CID,
         None),
        (CIRCUIT_TABLENAME,
         CIRCUIT_PID,
         PARAM_TABLENAME,
         PARAM_PID,
         None)]}

class Ta2ResultsSchema(ResultsSchema):

    def __init__(self):
        super(Ta2ResultsSchema, self).__init__()
        self.tablename_to_fieldtotype = TABLENAME_TO_FIELDTOTYPE
        self.tablename_to_requiredfields = TABLENAME_TO_REQUIREDFIELDS
        self.tablename_to_aux = TABLENAME_TO_AUX
        self.tablename_to_joins = TABLENAME_TO_JOINS
        self.performer_tablenames = PERFORMER_TABLENAMES
        self.other_tablenames_heirarchy = OTHER_TABLENAMES_HEIRARCHY
