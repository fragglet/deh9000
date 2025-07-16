from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField, FormField, FieldList
from wtforms.validators import DataRequired, NumberRange, Optional
from deh9000.tables import ammodata, miscdata, weaponinfo, states, mobjinfo

class AmmoForm(FlaskForm):
    max_ammo = IntegerField('Max Ammo', validators=[Optional()])
    per_ammo = IntegerField('Per Ammo', validators=[Optional()])

class MiscForm(FlaskForm):
    initial_health = IntegerField('Initial Health', validators=[Optional()])
    initial_bullets = IntegerField('Initial Bullets', validators=[Optional()])
    max_health = IntegerField('Max Health', validators=[Optional()])
    max_armor = IntegerField('Max Armor', validators=[Optional()])
    green_armor_class = IntegerField('Green Armor Class', validators=[Optional()])
    blue_armor_class = IntegerField('Blue Armor Class', validators=[Optional()])
    max_soulsphere = IntegerField('Max Soulsphere', validators=[Optional()])
    soulsphere_health = IntegerField('Soulsphere Health', validators=[Optional()])
    megasphere_health = IntegerField('Megasphere Health', validators=[Optional()])
    god_mode_health = IntegerField('God Mode Health', validators=[Optional()])
    idfa_armor = IntegerField('IDFA Armor', validators=[Optional()])
    idfa_armor_class = IntegerField('IDFA Armor Class', validators=[Optional()])
    idkfa_armor = IntegerField('IDKFA Armor', validators=[Optional()])
    idkfa_armor_class = IntegerField('IDKFA Armor Class', validators=[Optional()])
    bfg_cells_per_shot = IntegerField('BFG Cells Per Shot', validators=[Optional()])

class WeaponForm(FlaskForm):
    ammo_type = SelectField('Ammo Type', choices=[(str(i), name) for i, name in enumerate(ammodata.get_object_names())], validators=[Optional()])
    deselect_state = IntegerField('Deselect State', validators=[Optional()])
    select_state = IntegerField('Select State', validators=[Optional()])
    bobbing_state = IntegerField('Bobbing State', validators=[Optional()])
    shooting_state = IntegerField('Shooting State', validators=[Optional()])
    firing_state = IntegerField('Firing State', validators=[Optional()])

class StateForm(FlaskForm):
    sprite_number = IntegerField('Sprite Number', validators=[Optional()])
    sprite_subnumber = IntegerField('Sprite Subnumber', validators=[Optional()])
    duration = IntegerField('Duration', validators=[Optional()])
    next_state = IntegerField('Next State', validators=[Optional()])
    action_pointer = IntegerField('Action Pointer', validators=[Optional()])

class MobjForm(FlaskForm):
    doomednum = IntegerField('Doomed Number', validators=[Optional()])
    spawnstate = IntegerField('Spawn State', validators=[Optional()])
    spawnhealth = IntegerField('Spawn Health', validators=[Optional()])
    seestate = IntegerField('See State', validators=[Optional()])
    seesound = IntegerField('See Sound', validators=[Optional()])
    reactiontime = IntegerField('Reaction Time', validators=[Optional()])
    attacksound = IntegerField('Attack Sound', validators=[Optional()])
    painstate = IntegerField('Pain State', validators=[Optional()])
    painchance = IntegerField('Pain Chance', validators=[Optional()])
    painsound = IntegerField('Pain Sound', validators=[Optional()])
    meleestate = IntegerField('Melee State', validators=[Optional()])
    missilestate = IntegerField('Missile State', validators=[Optional()])
    deathstate = IntegerField('Death State', validators=[Optional()])
    xdeathstate = IntegerField('XDeath State', validators=[Optional()])
    deathsound = IntegerField('Death Sound', validators=[Optional()])
    speed = IntegerField('Speed', validators=[Optional()])
    radius = IntegerField('Radius', validators=[Optional()])
    height = IntegerField('Height', validators=[Optional()])
    mass = IntegerField('Mass', validators=[Optional()])
    damage = IntegerField('Damage', validators=[Optional()])
    activesound = IntegerField('Active Sound', validators=[Optional()])
    flags = IntegerField('Flags', validators=[Optional()])
    raisestate = IntegerField('Raise State', validators=[Optional()])

class PatchForm(FlaskForm):
    ammodata = FieldList(FormField(AmmoForm), min_entries=len(ammodata))
    miscdata = FormField(MiscForm)
    weaponinfo = FieldList(FormField(WeaponForm), min_entries=len(weaponinfo))
    states = FieldList(FormField(StateForm), min_entries=len(states))
    mobjinfo = FieldList(FormField(MobjForm), min_entries=len(mobjinfo))

    submit = SubmitField('Generate Patch')
