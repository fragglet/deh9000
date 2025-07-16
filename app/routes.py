from flask import render_template, request
from app import app
from app.forms import PatchForm
from deh9000.file import DehackedFile
from deh9000.tables import ammodata, miscdata, weaponinfo, states, mobjinfo

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PatchForm()
    patch_text = None
    if form.validate_on_submit():
        deh = DehackedFile()

        for i, ammo_form in enumerate(form.ammodata):
            if ammo_form.max_ammo.data is not None:
                deh.ammodata[i].maxammo = ammo_form.max_ammo.data
            if ammo_form.per_ammo.data is not None:
                deh.ammodata[i].perammo = ammo_form.per_ammo.data

        if form.miscdata.initial_health.data is not None:
            deh.miscdata.initial_health = form.miscdata.initial_health.data
        if form.miscdata.initial_bullets.data is not None:
            deh.miscdata.initial_bullets = form.miscdata.initial_bullets.data
        # ... and so on for all miscdata fields

        for i, weapon_form in enumerate(form.weaponinfo):
            if weapon_form.ammo_type.data:
                deh.weaponinfo[i].ammo = int(weapon_form.ammo_type.data)
            # ... and so on for all weaponinfo fields

        # States and Mobjinfo are more complex and will be handled similarly.
        # For now, this is a proof of concept.

        patch_text = "\n\n".join(deh.dehacked_diffs())

    return render_template('index.html', form=form, patch_text=patch_text, ammodata=ammodata, miscdata=miscdata, weaponinfo=weaponinfo, states=states, mobjinfo=mobjinfo)
