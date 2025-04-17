<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <h1>Instagram Clone API</h1>
    <h2>Description</h2>
    <p>
        The <strong>Instagram Clone API</strong> is a backend-only project built using Django and Django REST Framework (DRF). It replicates the core functionality of Instagram, such as user authentication, post creation, likes, comments, and following/unfollowing users. The system uses <strong>cookie-based authentication</strong> for secure session management.
    </p>
    <h2>Features</h2>
    <ul>
        <li><strong>User Registration & Login:</strong> Create an account and log in using secure, session-based cookies.</li>
        <li><strong>Profile Management:</strong> Update profile information and view other users’ profiles.</li>
        <li><strong>Post Creation:</strong> Create, retrieve, update, and delete image-based posts.</li>
        <li><strong>Like/Unlike Posts:</strong> Interact with posts through likes.</li>
        <li><strong>Comments:</strong> Add and view comments on posts.</li>
        <li><strong>Follow System:</strong> Follow and unfollow users to see their content.</li>
        <li><strong>Feed:</strong> View posts from followed users.</li>
    </ul>
    <h2>Tech Stack</h2>
    <ul>
        <li><strong>Backend:</strong> Django, Django REST Framework</li>
        <li><strong>Authentication:</strong> Session-based (cookie authentication)</li>
        <li><strong>Database:</strong> PostgreSQL or SQLite</li>
    </ul>
    <h2>Requirements</h2>
    <p>To run this project locally, ensure the following are installed:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Django 5.x</li>
        <li>Django REST Framework</li>
        <li>PostgreSQL or SQLite</li>
    </ul>
    <h2>Installation</h2>
    <ol>
        <li>Clone the repository:
            <pre><code>git clone https://github.com/vachhaniRahul/instagram_clone.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd instagram-clone-api</code></pre>
        </li>
        <li>Create a virtual environment:
            <pre><code>python -m venv venv</code></pre>
        </li>
        <li>Activate the virtual environment:
            <ul>
                <li>On Windows:
                    <pre><code>.\venv\Scripts\Activate.ps1</code></pre>
                </li>
                <li>On macOS/Linux:
                    <pre><code>source venv/bin/activate</code></pre>
                </li>
            </ul>
        </li>
        <li>Install dependencies:
            <pre><code>pip install -r requirements.txt</code></pre>
        </li>
        <li>Apply migrations:
            <pre><code>python manage.py migrate</code></pre>
        </li>
        <li>Create a superuser:
            <pre><code>python manage.py createsuperuser</code></pre>
        </li>
        <li>Run the development server:
            <pre><code>python manage.py runserver</code></pre>
        </li>
    </ol>
    <h2>API Usage</h2>
    <ul>
        <li>Use tools like <strong>Postman</strong> or <strong>cURL</strong> to interact with the API endpoints.</li>
        <li>All authentication is handled via <strong>cookie-based sessions</strong>.</li>
        <li>Example endpoints:
            <ul>
                <li><code>/api/register/</code> – User registration</li>
                <li><code>/api/login/</code> – Login and receive session cookie</li>
                <li><code>/api/logout/</code> – Logout and destroy session</li>
                <li><code>/api/posts/</code> – Create/view posts</li>
                <li><code>/api/comments/</code> – Add/view comments</li>
                <li><code>/api/follow/</code> – Follow/unfollow a user</li>
                <li><code>/api/feed/</code> – View posts from followed users</li>
            </ul>
        </li>
    </ul>
    <h2>Admin Panel</h2>
    <ul>
        <li>Access the Django admin panel at <strong>http://127.0.0.1:8000/admin/</strong> to manage users and posts.</li>
    </ul>
</body>
</html>
