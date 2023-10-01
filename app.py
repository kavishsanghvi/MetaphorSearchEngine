from flask import Flask, render_template, request, redirect, url_for
from metaphor_python import Metaphor

app = Flask(__name__)

# Replace with your Metaphor API key
METAPHOR_API_KEY = 'fd22b50b-c264-4068-a9ac-8a53d5302ab0'

# Initialize the Metaphor client
metaphor = Metaphor(api_key=METAPHOR_API_KEY)


@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        num_results = 30  # You can customize the number of results
        include_domains = None  # Customize as needed
        exclude_domains = None  # Customize as needed
        start_crawl_date = None  # Customize as needed
        end_crawl_date = None  # Customize as needed
        start_published_date = None  # Customize as needed
        end_published_date = None  # Customize as needed
        use_autoprompt = False  # Customize as needed
        search_type = 'neural'  # You can use 'keyword' or 'neural'

        # Perform the Metaphor search
        search_response = metaphor.search(
            query=query,
            num_results=num_results,
            include_domains=include_domains,
            exclude_domains=exclude_domains,
            start_crawl_date=start_crawl_date,
            end_crawl_date=end_crawl_date,
            start_published_date=start_published_date,
            end_published_date=end_published_date,
            use_autoprompt=use_autoprompt,
            type=search_type
        )

        # Render the search results
        return render_template('results.html', search_response=search_response)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
