# Data-Source-API-Analyst-Test
Homework assignment for Data Source API Analyst role.

## Purpose of the Test
The primary goal of this test is to demonstrate the ability to interact with the GitHub API, extract data according to client needs, and effectively handle challenges like rate limits, pagination, and authentication. The test is divided into logical steps, each focusing on key aspects of working with APIs and delivering a robust solution.

---

## Documentation of Approach

### **Step 1: Prepare & Test a List of Reports**

#### Client Needs:
- **Search Repositories** (public): Identify and retrieve relevant repositories.
- **Commits**: Extract commit history for the desired repositories.
- **Contents**: Access repository files and content.

#### Approach:
1. **Research GitHub API**:
   - Review the official [GitHub API documentation](https://docs.github.com/en/rest) to identify relevant endpoints.
   - Understand request structures, pagination mechanisms, rate limits, and error handling.
2. **Endpoint Identification**:
   - Search repositories: `/search/repositories`
   - List commits: `/repos/{owner}/{repo}/commits`
   - Get contents: `/repos/{owner}/{repo}/contents/{path}`

---

### **Step 2: Set Up a GitHub Repository**

#### Repository Creation:
- **Name**: `Data-Source-API-Analyst-Test`
- **Description**: "Homework assignment for Data Source API Analyst role."
- **Visibility**: Public for transparency and collaboration.

#### Repository Structure:
├── README.md: Purpose, approach, and reflections. 
├── Content/
│ ├── API_Documentation.md: Overview of endpoints, usage, and examples.
│ ├── auth_process.py: Python code for authentication.
│ ├── data_extraction.py: Scripts for data extraction, error handling, and pagination.
│ ├── troubleshooting_guide.md: Common issues and resolutions.
├── Postman_Collection/
      │ ├── github_api_test.postman_collection.json: Postman requests for API testing.
      │ ├── colab_notebook.ipynb: Notebook for API data extraction.


#### Initial Commit:
Include the folder structure and a basic `README.md` to provide project context.

---

### **Step 3: Create a Postman Collection or Google Colab Notebook for API Extraction**

#### Postman Setup:
1. **Create Collection**: `Github API Test`.
2. **Define Folders**:
   - `Auth`: Authentication requests.
   - `Requests`: API calls for repositories, commits, and content.
3. **Environment Variables**:
   - `Authorization`: Token for API requests.
   - `X-GitHub-Api-Version`: Specify the version of the API.
4. **Request Testing**:
   - Test each endpoint and save responses for validation.

#### Colab Setup (Bonus Points):
1. **Authentication**:
   - Use `requests` or `httpx` libraries for API calls.
   - Implement a reusable function for authentication.
2. **Data Extraction**:
   - Write functions to handle pagination and error handling.
   - Iterate over paginated responses to extract complete data.
3. **Response Validation**:
   - Print sample responses for verification.

---

### **Step 4: Troubleshooting Guide**

#### Common Issues & Solutions:
- **401 Unauthorized**:
  - Verify the `AUTH_TOKEN` or access token.
  - Ensure correct setup of environment variables in Postman or Colab.
- **Rate Limits**:
  - Check API headers for rate limit status.
  - Implement backoff logic to retry requests after rate reset.
- **Pagination**:
  - Follow the `Link` header for next pages or iterate over responses with `page` parameters.

---

### **Step 5: Get Results**

#### Save Final Outputs:
1. **Postman**:
   - Export the collection as `github_api_test.postman_collection.json`.
   - Upload to the repository under `Postman_Collection/`.
2. **Colab**:
   - Download the notebook as `colab_notebook.ipynb`.
   - Add to `Postman_Collection/`.

---

### Reflection
Include your thoughts on the process, challenges faced, and areas for improvement in the `README.md` file under the "Reflection" section.
