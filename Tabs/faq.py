import streamlit as st
import pandas as pd
def app(df):
    st.title('FAQ Demo')
     # Sidebar chatbot integration
    st.markdown("## Cloud Consultant 💻")
    chatbot_html = '''
        <iframe style="background: white;border-radius: 8px; border: none; box-shadow: 5px 5px 24px 0px #0000001F;" src="https://embed.writer.com/chat/TlXwppNI-QxsnlIoWV6cUcPysAxorREivVHIfjHeDWo" width="100%" height="600"></iframe>
    '''
    st.markdown(chatbot_html, unsafe_allow_html=True)


    df = pd.read_csv('cloud_security_dataset.csv')
    st.subheader('The database 🫙')
    st.dataframe(df)
  

    st.markdown('''Here is an explanation of the database provided containing a wide range of fields related to access control, security, and user management within cloud or IT environments. Here's a breakdown of the different fields and what they represent:

### **Categories/Columns:**

1. **Authentication_Mechanisms:** 
   - Specifies the type of authentication used for identity verification. E.g., "Biometric."

2. **Authorization_Models:** 
   - Defines the model used to determine what a user can access. E.g., PBAC (Policy-Based Access Control) or ABAC (Attribute-Based Access Control).

3. **User_Identity_Management:** 
   - A flag (TRUE/FALSE) that indicates whether user identity management is in place. This ensures users are properly managed through identity platforms.

4. **Access_Levels:** 
   - The permissions or control a user has, such as "Admin" or "Write" access.

5. **User_Roles:** 
   - Defines the role of the user in the system, such as "Admin" or "Guest."

6. **Security_Policies:** 
   - A flag (TRUE/FALSE) indicating if security policies are implemented.

7. **Compliance_Requirements:** 
   - Shows if the system complies with external or internal security requirements (TRUE/FALSE).

8. **User_Session_Management:** 
   - Indicates whether user sessions are actively managed and monitored for security (TRUE/FALSE).

9. **Privileged_Access_Management:** 
   - Ensures control over privileged users who have higher access (TRUE/FALSE).

10. **Third_Party_Integrations:** 
    - Specifies if third-party integrations are supported or allowed in the environment (TRUE/FALSE).

11. **Cloud_Service_Provider:** 
    - Identifies the cloud provider in use, such as "GCP" (Google Cloud Platform) or "IBM Cloud."

12. **Geolocation_Restrictions:** 
    - Indicates if there are location-based access restrictions, such as access being limited to the US.

13. **Time_Based_Access:** 
    - TRUE/FALSE flag for implementing time-based access control to restrict or allow access during specific times.

14. **User_Behavior_Analytics:** 
    - Shows whether the system monitors user behavior for anomalies (TRUE/FALSE).

15. **Network_Security_Controls:** 
    - Refers to controls in place to secure the network (TRUE/FALSE).

16. **Access_Control_Lists (ACLs):** 
    - Defines whether ACLs are implemented to regulate network access (TRUE/FALSE).

17. **Encryption_Policies:** 
    - Indicates if data encryption policies are enforced (TRUE/FALSE).

18. **Data_Sensitivity_Classification:** 
    - Refers to whether data is classified based on sensitivity (e.g., Private/Public).

19. **Logging_and_Monitoring:** 
    - TRUE/FALSE flag indicating whether activity logging and monitoring are active.

20. **Security_Groups:** 
    - Whether security groups are used to control traffic within the cloud environment (TRUE/FALSE).

21. **Identity_Federation:** 
    - Shows if identity federation across multiple domains or systems is enabled (TRUE/FALSE).

22. **Least_Privilege_Principle:** 
    - Indicates adherence to the principle of least privilege, where users only have access to what they need (TRUE/FALSE).

23. **Access_Control_Propagation:** 
    - Refers to whether access control policies propagate through different layers of the system (TRUE/FALSE).

24. **API_Access_Control:** 
    - Specifies if there are specific access control measures for APIs (TRUE/FALSE).

25. **Cloud_Workload_Identity:** 
    - Ensures that workloads in the cloud are given appropriate identities for security purposes (TRUE/FALSE).

26. **Audit_Trails:** 
    - Indicates if the system maintains audit logs for activities (TRUE/FALSE).

27. **Access_Revocation:** 
    - Describes whether access can be revoked when necessary (TRUE/FALSE).

28. **Cross_Region_Access:** 
    - Shows if cross-region access is allowed (TRUE/FALSE).

29. **DLP_Policies:** 
    - Describes if Data Loss Prevention (DLP) policies are implemented (TRUE/FALSE).

30. **Multi_Tenancy_Security:** 
    - Refers to whether there are security mechanisms in place for a multi-tenant environment (TRUE/FALSE).

31. **Cloud_Orchestration_Layer_Security:** 
    - Indicates if there are specific security measures for the cloud orchestration layer (TRUE/FALSE).

32. **Token_Based_Access_Control:** 
    - Specifies if access control is based on tokens (TRUE/FALSE).

33. **Access_Control_Policies_for_Serverless:** 
    - Refers to access control policies specifically for serverless computing (TRUE/FALSE).

34. **Granular_Access_Control:** 
    - Describes whether fine-grained access control measures are in place (TRUE/FALSE).

35. **Cloud_Native_Directory_Services:** 
    - Refers to whether the system uses cloud-native directory services for managing access (TRUE/FALSE).

36. **Access_to_Logs_and_Monitoring_Tools:** 
    - Indicates whether users can access logging and monitoring tools (TRUE/FALSE).

37. **Custom_Access_Control_Policies:** 
    - Whether custom access control policies are allowed in the system (TRUE/FALSE).

38. **Zero_Trust_Architecture:** 
    - Refers to the adoption of a Zero Trust Architecture model for security (TRUE/FALSE).

39. **Infrastructure_as_Code:** 
    - Describes if infrastructure is managed as code, ensuring automation and versioning (TRUE/FALSE).

40. **VPC_Controls:** 
    - Refers to security controls related to the Virtual Private Cloud (TRUE/FALSE).

41. **Segmentation_of_Duties:** 
    - Describes if duties and roles are appropriately segmented to reduce risk (TRUE/FALSE).

42. **Instance_Metadata_Service_Access:** 
    - Indicates if access to metadata services is controlled for cloud instances (TRUE/FALSE).

43. **Shared_Responsibility_Model:** 
    - Shows whether the shared responsibility model between provider and customer is enforced (TRUE/FALSE).

44. **Cloud_Storage_Access_Policies:** 
    - Describes if specific access policies exist for cloud storage services (TRUE/FALSE).

45. **Data_Governance_Framework:** 
    - Indicates if a data governance framework is in place (TRUE/FALSE).

46. **API_Gateway_Security:** 
    - Refers to security measures applied to API gateways (TRUE/FALSE).

47. **Dynamic_Access_Management:** 
    - Whether dynamic access management policies are in place (TRUE/FALSE).

48. **Account_Lockout_Policies:** 
    - Indicates if account lockout policies are enforced after repeated unsuccessful login attempts (TRUE/FALSE).

49. **Access_to_Sensitive_Compute_Resources:** 
    - Describes whether access to sensitive compute resources is controlled (TRUE/FALSE).

50. **Penetration_Testing_and_Vulnerability_Assessments:** 
    - Indicates whether penetration testing and vulnerability assessments are regularly conducted (TRUE/FALSE).

51. **Industry:** 
    - Represents the industry that the organization or system is serving, such as "Community Services" or "Disaster Recovery."

52. **Security_Score:** 
    - A security rating or score (e.g., 3) that might reflect the overall security compliance or health of the system.

### **Example Rows:**
- The first row corresponds to a system with Biometric authentication, Policy-Based Access Control (PBAC), managed user identities, high privileges (Admin), and adherence to various security and compliance measures on Google Cloud Platform (GCP) with location restrictions (US).
  
- The second row shows a system using Biometric authentication, Attribute-Based Access Control (ABAC), with Write access for Guest users, and hosted on IBM Cloud with similar but slightly different security measures. 

These fields represent a highly detailed structure for managing security, access control, compliance, and cloud-based services. This kind of database can be used for managing and assessing security controls, policies, and compliance across different cloud or IT infrastructures.''')

