Simple test
------------

Ensure your device works with this simple test.

.. literalinclude:: ../examples/keymanager_simpletest.py
    :caption: examples/keymanager_simpletest.py
    :linenos:

Keys
----

Use a digital input to trigger a note.

.. literalinclude:: ../examples/keymanager_keys.py
    :caption: examples/keymanager_keys.py
    :linenos:

Arpeggiator
-----------

Demonstration of the arpeggiator.

.. literalinclude:: ../examples/keymanager_arpeggiator.py
    :caption: examples/keymanager_arpeggiator.py
    :linenos:

Sequencer
---------

Demonstration of the sequencer.

.. literalinclude:: ../examples/keymanager_sequencer.py
    :caption: examples/keymanager_sequencer.py
    :linenos:

synthio & MIDI
--------------

Use the :class:`relic_keymanager.Keyboard` class to help allocate MIDI notes into a limited set of
:class:`synthio.Note` objects using USB MIDI input and DAC/PWM audio playback.

.. literalinclude:: ../examples/keymanager_synthio.py
    :caption: examples/keymanager_synthio.py
    :linenos:
