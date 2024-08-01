from langchain_core.runnables import chain

from redbox.models.chain import ChainState
from redbox.models.chat import ChatResponse
from redbox.transform import map_document_to_source_document


@chain
def map_to_chat_response(state: ChainState):
    """
    Create a ChatResponse at the end of a chain from a dict containing
    'response' a string to use as output_text
    'source_documents' a list of documents to map to source_documents
    """
    return ChatResponse(
        output_text=state["response"],
        source_documents=[map_document_to_source_document(d) for d in state.get("documents") or []],
        route_name=state["route_name"],
    )
