from pygments.style import Style
from pygments.token import *

__all__ = ['MyThesis', 'MyThesisBW']

class MyThesis(Style):
    default_style = ""

    styles = {
        Keyword:                'bold #7F0055',
        String:                 '#2A00FF',
	String.Escape:          'bold',

        # // ... and /* ... */
        Comment:                '#3F7F5F',

        # /** ... */
        Comment.Doc:             '#3F5FBF',


        Number:                 'bold #60E',

        # Lifetime Substitution
        Name.LifetimeSubstitution: 'bold #E06',
    }


class MyThesisBW(Style):
    default_style = ""

    styles = {
        Keyword:                'bold',
	String.Escape:          'bold',
        Number:                 'bold',
        Name.LifetimeSubstitution: 'bold',
    }
