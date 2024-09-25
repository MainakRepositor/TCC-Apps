"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Cloud Security Architecture Analysis System")

    # Add image to the home page
    st.image("./images/home.png",width=1000)

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Cloud Security and Cloud Score

Cloud security involves a broad set of policies, technologies, and controls designed to protect data, applications, and the cloud infrastructure from threats and vulnerabilities. Effective cloud security ensures that resources hosted in the cloud are safe from unauthorized access, data breaches, and service disruptions.

### Key Aspects of Cloud Security:
1. **Data Protection:** Encryption of data at rest and in transit ensures that sensitive information is safeguarded. Access control measures, such as Identity and Access Management (IAM), help manage who has access to cloud resources.
   
2. **Threat Detection:** Cloud providers offer monitoring tools to detect anomalies or security threats in real-time. These tools leverage AI and machine learning for better threat intelligence.
   
3. **Compliance and Governance:** Most cloud providers are compliant with industry standards like GDPR, HIPAA, and ISO 27001. This helps ensure regulatory requirements are met.
   
4. **Network Security:** Firewalls, VPNs, and network segmentation are used to isolate and protect cloud environments from attacks like Distributed Denial of Service (DDoS).
   
5. **Identity and Access Management (IAM):** IAM tools provide role-based access to ensure that users have the appropriate level of access, reducing the risk of insider threats.
   
6. **Continuous Monitoring:** Cloud providers offer services for continuous monitoring and logging to identify and remediate security incidents quickly.

### Guessing a Cloud Security Score:
A cloud security score is often determined by a combination of several factors. Cloud security tools like AWS Security Hub or Microsoft Secure Score provide insights into a cloud environment’s security posture. The score typically reflects the following:

1. **Compliance Adherence:** The extent to which your cloud environment follows industry compliance regulations.
2. **Access Control Effectiveness:** How well IAM policies are enforced and whether users have minimal necessary privileges.
3. **Network and Infrastructure Security:** How secure the cloud network and infrastructure are, including proper firewall configurations and network isolation practices.
4. **Incident Response and Monitoring:** How well the cloud environment is set up for detecting and responding to security incidents.
5. **Data Encryption:** Whether data is encrypted both in transit and at rest, and if the encryption algorithms meet current security standards.

Cloud providers may give you a score based on the percentage of security best practices followed, the number of misconfigurations found, or the severity of vulnerabilities detected. Regular audits, compliance checks, and automated security assessments are ways to improve your cloud score.

The cloud score can be used as a benchmark for improving your cloud security by following best practices and ensuring continuous monitoring and compliance with security standards.
        </p>
    """, unsafe_allow_html=True)
