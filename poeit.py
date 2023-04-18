import poetrytools as pt

from flask import Flask, request, jsonify
app = Flask(__name__)


@app.get('/')
def get_meter():
    return jsonify({
        'form': 'form',
        'lines': 0,
        'meter': 'meter',
        'rhyme_scheme': 'scheme',
        'rhyme_type': 'type',
        'stanza': 'stanza',
        'stanza_lengths': '0,0',
        'stress': ['01'],
        'syllables': 0
    })


@app.post('/')
def post_meter():
    msg = request.get_json()['message']
    poem = pt.tokenize(msg)
    rhyme_scheme, rhyme_type = pt.guess_rhyme_type(poem)
    stress, lines, syllables, metre = pt.guess_metre(poem)
    stanza_lengths, stanza = pt.guess_stanza_type(poem)
    return jsonify({
        'form': pt.guess_form(poem),
        'lengths': stanza_lengths,
        'lines': lines,
        'meter': metre,
        'rhyme_scheme': rhyme_scheme,
        'rhyme_type': rhyme_type,
        'stanza': stanza,
        'stress': stress,
        'syllables': syllables
    })
