### 🫵 **!! USE THIS TUTORIAL AS A BASIS !!** 👇

<https://docs.godotengine.org/en/stable/getting_started/first_3d_game/>

That way we keep our structure and naming fairly standardized. We're not familiar enough to start fiddling toooo much 🙃

___ 

## NOTES

Each animal is a "player" object. Please refer and name them in the manner like ``bird_player``.

Define the player as a player.

Each level is a "scene". Please refer and name them in the manner like ``bird_level``. We need to figure out how to transition seamlessy between scenes.

Each ``player`` has a camera attached to it, with it's own pitch and twist angles available. If it's possible to interpolate between cameras, this should make it trivial to switch.

To correct so that the coordinate-system is relevant to the camera, we multiply the ``pitch-basis`` with the ``input_force``.

## The transitions can work as follows:

- The player reaches a threshold, where they will lose control of their inputs.

- Letterboxing happens, and the controls are pre-emptively programmed.

- In the level, we place another ``transition camera``, which has the movements of the transition programmed. We then intorpolate *from* the ``player camera`` *to* the ``transition`` camera.

- as this animation happens, we load the next section. When everything is prepped, we interpolate from the ``transition camera``  to the new animals ``player camera``.

- Letterboxing closes, and the player has control back.

___

Shaders will be implemented at the end of development.

- Everything is colored "naturally" before shaders.

- Perhaps a slight curvature-shader on the entire viewport.

    - This will reinforce the circular theme; going around a globular world.

Animation should be handled programattically. 


