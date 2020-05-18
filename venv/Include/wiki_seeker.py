# import queue
import wikipedia
import random

# game description:
# given a destination point (destination article), get there from a random start point (start article).
# show the article path that was used to get there


def wiki_seeker(destination_article):
    start_article = wikipedia.random()
    print("Starting at: {}".format(start_article))
    search(start_article, destination_article, step=0)


def search(start_point, dest_point, step):
    if start_point != dest_point:
        print("step {0} is: {1}".format(str(step), start_point))
        next_point = get_next_point(start_point)
        search(next_point, dest_point, step+1)
    else:
        print("Finished! got to {0} in {1} steps.".format(dest_point, str(step)))


# chooses next randomly. can be changed when necessary
def get_next_point(start_point):
    next_point = choose_next_randomly(start_point)
    return next_point


def choose_next_randomly(wiki_point):
    wiki_page = get_wiki_page(wiki_point)
    wiki_page_refs = wiki_page.links
    random.shuffle(wiki_page_refs)
    next_point = get_valid_point(wiki_page_refs[0], wiki_page_refs)
    return next_point


def get_valid_point(point_in_question, options):
    valid_page = get_wiki_page(point_in_question, options)
    valid_point = valid_page.title
    return valid_point


def get_wiki_page(article_name, options=None):
    try:
        wiki_page = wikipedia.page(title=article_name)
        return wiki_page
    except wikipedia.exceptions.DisambiguationError as err:
        wiki_title = err.options[0]  # always take the first option
        wiki_page = get_wiki_page(wiki_title, options)
        return wiki_page
    except wikipedia.exceptions.PageError:
        if options is not None and len(options) > 0:
            # TODO: how to prevent infinite loop here?
            random.shuffle(options)
            wiki_title = options[0]
            wiki_page = get_wiki_page(wiki_title, options)
        else:
            wiki_page = get_wiki_page(wikipedia.random())
        return wiki_page



# wikipedia.set_lang("he")
# wiki_seeker("צבא הגנה לישראל")
