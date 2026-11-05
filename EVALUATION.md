# Agent Lab Part 4 – Code Evaluation

## 1. AI Prompt Used for Testing

I used ChatGPT to help generate automated Python tests for my Campus Resource Assistant.

My prompt requested five tests using Python's `assert` statements to verify the following:

- Successful library lookup
- Tutoring alias lookup
- Case-insensitive searches
- Error handling for unavailable resources
- Listing all available campus resources

I also provided my existing `agent.py` code so the generated tests could use the correct function and return structure.

## 2. Test Code and Functionality

I created `campus_agent/test_agent.py` containing five automated tests.

The tests call `get_campus_resource_info()` and verify that the function returns the expected information.

The library tests check for "Cattaraugus County Campus Library," while the tutoring test checks for "Learning Center."

The remaining tests verify error handling and confirm that at least four campus resources are available.

## 3. Testing Results and Verification

When I initially ran my tests through GitHub Actions, two tests passed and three failed.

The failures occurred because the AI-generated tests expected the generic names "Library" and "Tutoring Center," but my actual JSON data used different names.

After correcting the expected values, I pushed the changes to GitHub and reran the automated tests.

**Final result: All five tests passed.**

I also tested the deployed Streamlit application by asking where the library was located. The assistant successfully returned the library's location, contact information, hours guidance, and website.

## 4. Changes Made and Why

I modified three assertions in `test_agent.py`.

The original assertions expected:

- Library
- Tutoring Center

I changed them to:

- Cattaraugus County Campus Library
- Learning Center

These changes were necessary because the tests needed to reflect the actual names stored in `campus_resources.json`.

I chose to correct the tests rather than modify the resource data because the application was already returning the intended campus information.

## 5. AI Prompt Used for CI/CD

I used ChatGPT to generate a GitHub Actions workflow for my existing repository.

I requested a YAML workflow that would run automatically whenever code was pushed to the `main` branch.

The workflow needed to use Ubuntu, Python 3.11, install pytest and the application dependencies, and execute the five automated tests.

## 6. Final CI/CD Workflow

I created `.github/workflows/test.yml` in the root of my GitHub repository.

The workflow performs the following operations:

1. Checks out the repository using GitHub Actions.
2. Configures Python 3.11.
3. Installs pytest and the project dependencies.
4. Runs the tests inside the `campus_agent` directory.
5. Reports whether the tests passed or failed.

After correcting the test assertions, GitHub Actions successfully completed all five tests.

## 7. CI/CD Changes and Evaluation

The workflow was designed to work with my existing repository structure.

Because my Python application and test file are inside the `campus_agent` directory, the workflow installs dependencies from that folder and runs pytest from the correct working directory.

I verified the workflow by reviewing the GitHub Actions logs.

I also verified continuous deployment through Streamlit Community Cloud.

After pushing a small change to `app.py`, the Streamlit deployment logs showed that the platform pulled changes from GitHub, processed dependencies, and updated the application automatically.

## 8. Reflection

### Was the AI-generated code better or worse than what I would write?

The AI-generated code was helpful because it provided a clear starting point and saved time writing repetitive tests and workflow configuration.

However, it was not completely accurate on the first attempt. Three tests failed because the expected resource names did not match my actual data.

This showed me that AI-generated code still requires human review and testing.

### Did I find code erosion or verbosity?

I did not notice significant code erosion or unnecessary verbosity in the generated tests. Each test had a clear purpose, and the code was relatively simple.

The biggest issue was accuracy rather than complexity. The AI used generic expected names instead of the names in my resource data.

This connects to SlopCodeBench because it demonstrates why developers must evaluate generated code instead of assuming it is correct.

### What would I do differently next time?

Next time, I would provide the AI with both my Python source code and the actual JSON data before requesting tests.

I would also ask the AI to verify that every assertion matches the existing data and to avoid unnecessary code or duplicated logic.

This would help reduce errors and improve the quality of the generated code.

### What impact could this application have on JCC students?

The Campus Resource Assistant could make it easier for JCC students to find information about important campus services.

Instead of searching through multiple webpages, students could ask questions about the library, tutoring, advising, or financial aid and receive information in one place.

This could save students time, improve access to campus resources, and help new students become more familiar with the college.

The automated testing and deployment system also makes the application easier to maintain. Updates can be tested automatically, helping developers identify problems before they affect students.

## 9. Final Evaluation

This project helped me understand the importance of automated testing, continuous integration, and continuous deployment.

I learned that getting code to run is only one part of software development. It is also important to verify that the code behaves correctly, identify errors, and maintain a reliable deployment process.

Using AI helped speed up development, but reviewing and correcting the generated code was still my responsibility.

Overall, the project gave me practical experience with Python testing, GitHub Actions, Streamlit Cloud, and evaluating AI-generated code.
