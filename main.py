import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Jay Sim")
    content = "Jay Sim, based in Vancouver, British Columbia, is a certified DevOps engineer " \
              "with proficiency in cloud platforms including AWS, Azure, GCP, and Exoscale. " \
              "He boasts an extensive programming background with languages like Python, JavaScript, and Bash scripting. " \
              "Jay is adept in leveraging DevOps tools like Kubernetes, Terraform, and Prometheus. His experience spans " \
              "orchestrating CI/CD pipelines with GitLab, managing AWS resources, and setting up comprehensive monitoring systems. " \
              "He's also previously automated sales reports for multi-million custom orders in a sales role. " \
              "A graduate with distinction from Capilano University in Tourism Management, " \
              "Jay also completed The Web Developer Bootcamp in 2022, producing a full-stack web application project. Fluent in both English and Korean, " \
              "Jay's diverse skill set is underscored by certifications such as AWS Solutions Architect, Terraform Associate, and Certified Kubernetes Administrator."
    st.info(content)

mainContent = "Lorem Ipsum is simply dummy text of the printing and " \
              "typesetting industry. Lorem Ipsum has been the " \
              "industry's standard dummy text ever since the 1500s, " \
              "when an unknown printer took a galley of type and scrambled " \
              "it to make a type specimen book. It has survived not only five " \
              "centuries, but also the leap into electronic typesetting, " \
              "remaining essentially unchanged. It was popularised in the " \
              "1960s with the release of Letraset sheets containing Lorem " \
              "Ipsum passages, and more recently with desktop publishing " \
              "software like Aldus PageMaker " \
              "including versions of Lorem Ipsum."

st.write(mainContent)
