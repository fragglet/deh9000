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

        # Ammo data
        for i, ammo_form in enumerate(form.ammodata):
            if ammo_form.max_ammo.data:
                deh.ammodata[i].maxammo = ammo_form.max_ammo.data
            if ammo_form.per_ammo.data:
                deh.ammodata[i].perammo = ammo_form.per_ammo.data

        # Misc data
        for field_name, field in form.miscdata._fields.items():
            if field.type != 'CSRFTokenField' and field.data is not None:
                setattr(deh.miscdata, field_name, field.data)

        patch_text = "\n\n".join(deh.dehacked_diffs())

    return render_template('index.html', form=form, patch_text=patch_text, ammodata=ammodata, miscdata=miscdata, weaponinfo=weaponinfo, states=states, mobjinfo=mobjinfo)
