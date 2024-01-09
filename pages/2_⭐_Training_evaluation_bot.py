from dotenv import load_dotenv

load_dotenv()

import utils
import streamlit as st
from streaming import StreamHandler

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from trainer import training_evaluation_prompt as PROMPT


nm = "Training Evaluation Module"

st.set_page_config(page_title=nm, page_icon="⭐")
st.header(nm)


class ContextChatbot:
    def __init__(self):
        # utils.configure_openai_api_key()
        self.openai_model = "gpt-3.5-turbo"

    @st.cache_resource
    def setup_chain(_self):
        memory = ConversationBufferMemory()
        llm = OpenAI(model_name=_self.openai_model, temperature=0, streaming=True)
        chain = ConversationChain(llm=llm, memory=memory, verbose=True, prompt=PROMPT)
        return chain

    @utils.enable_chat_history
    def main(self):
        chain = self.setup_chain()
        user_query = st.chat_input(placeholder="Ask me anything!")
        if user_query:
            utils.display_msg(user_query, "user")
            with st.chat_message("assistant"):
                st_cb = StreamHandler(st.empty())
                response = chain.run(user_query, callbacks=[st_cb])
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )


if __name__ == "__main__":
    obj = ContextChatbot()
    obj.main()
