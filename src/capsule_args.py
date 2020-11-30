from config import VOCAB_SIZE, EMBEDDING_SIZE, NUM_CLASS

NUM_CODEBOOK = 8
NUM_CODEWORD = None
HIDDEN_SIZE = 256
IN_LENGTH = 8
OUT_LENGTH = 16
ROUTING_TYPE = 'dynamic'
EMBEDDING_TYPE = "cwc"
CLASSIFIER_TYPE = "capsule"
NUM_ITERATIONS = 3
NUM_REPEAT = None
DROP_OUT = 0.5

LOSS_TYPE = "mf"