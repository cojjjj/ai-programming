# Agent Lab Part 4 – Project Evaluation

## 1. Testing Approach

The main objective of this lab was to improve the reliability of my Campus Resource Assistant by implementing automated testing and a continuous integration and deployment workflow.

I focused on verifying that the resource lookup function returned accurate information, handled different inputs correctly, and provided useful error messages when a resource was unavailable.

I implemented five tests covering library lookup, tutoring aliases, case-insensitive searches, invalid resource requests, and listing all available resources.

## 2. Test Implementation

I created a Python test file named `test_agent.py` using assertions to verify the behavior of the `get_campus_resource_info()` function.

Each test checks a specific requirement rather than attempting to test the entire application at once. This approach makes it easier to identify problems and determine which part of the application needs attention.

The tests are deterministic because they operate on locally stored JSON data without requiring an API connection or language model response.

## 3. Testing Results

During the initial GitHub Actions test run, two tests passed and three failed.

After reviewing the failure logs, I determined that the problem was not with the resource lookup function itself. The tests were expecting generic resource names that did not match the actual values stored in my JSON file.

For example, the library test expected "Library," while the application returned "Cattaraugus County Campus Library." The tutoring test had a similar issue because the actual resource name was "Learning Center."

I corrected the expected values and ran the workflow again. All five tests passed successfully.

This experience demonstrated the importance of reviewing test failures carefully instead of immediately assuming the application code is incorrect.

## 4. Changes and Improvements

The primary changes involved correcting three test assertions to match the actual campus resource data.

I kept the existing resource lookup function unchanged because it was already returning the correct information.

This was an important distinction because modifying working application code to satisfy incorrect test expectations could introduce unnecessary problems.

I also organized the testing process so that each test verifies one specific behavior, making the code easier to maintain and troubleshoot.

## 5. Continuous Integration

I configured GitHub Actions using a workflow file located at `.github/workflows/test.yml`.

The workflow automatically runs whenever changes are pushed to the main branch of my repository.

It checks out the repository, configures Python 3.11, installs the required dependencies, and executes the automated tests using pytest.

After resolving the assertion errors, the workflow completed successfully with all five tests passing.

This setup helps identify potential issues whenever changes are made to the project.

## 6. Continuous Deployment

I deployed the Campus Resource Assistant using Streamlit Community Cloud and connected it to my GitHub repository.

I configured the application's Google API key through Streamlit Secrets instead of storing sensitive credentials directly in the repository.

After confirming that the application loaded successfully, I tested it by asking for the location of the campus library.

The assistant returned the library's location, phone number, hours information, and website.

I also tested automatic redeployment by committing a small change to `app.py`. Streamlit detected the updated repository, processed the dependencies, and updated the application without requiring a manual deployment.

## 7. Code Quality Evaluation

One of the most important lessons from this lab was that functioning code and reliable code are not necessarily the same thing.

The initial tests were structured correctly, but some assertions contained incorrect expectations. Even though the code was syntactically valid, the tests could not pass until those expectations were corrected.

I also considered the concepts of code erosion and verbosity discussed in SlopCodeBench.

I did not identify significant unnecessary complexity or duplication in the final test file. Each function has a specific purpose, and the assertions are straightforward.

The main improvement was ensuring that the tests accurately represented the application's existing data and behavior.

## 8. Reflection

This lab gave me a better understanding of how testing and automation fit into real software development.

Before implementing the workflow, testing required manually executing commands and reviewing the results. With GitHub Actions, the process is automated whenever changes are pushed to the repository.

The most useful part of the assignment was troubleshooting the failed tests. I had to review the error messages, compare the expected values against the actual results, and determine whether the problem was in the application or the tests.

In future projects, I would review the source data and expected outputs before writing assertions. I would also consider adding more automated checks, such as code linting, security scanning, and test coverage reporting.

From a cybersecurity perspective, I also recognize the importance of protecting API credentials and keeping sensitive configuration information outside public repositories.

## 9. Impact on JCC Students

The Campus Resource Assistant could provide a convenient way for students to access information about campus services without having to navigate multiple webpages.

Students could ask questions about the library, tutoring, advising, or financial aid and receive information through a simple interface.

This could be especially useful for new students who are unfamiliar with the campus and its available resources.

The automated testing and deployment process also helps support the application's long-term reliability by making updates easier to verify and release.

## 10. Conclusion

Overall, this project provided practical experience with Python testing, GitHub Actions, CI/CD workflows, and Streamlit deployment.

The biggest takeaway was learning how to identify and resolve problems through testing rather than making unnecessary changes to working code.

By the end of the lab, I had five passing automated tests, a functioning GitHub Actions workflow, and a deployed Streamlit application that successfully updated when changes were pushed to GitHub.

The project reinforced how important testing, troubleshooting, automation, and secure configuration practices are when developing applications intended for real users.
