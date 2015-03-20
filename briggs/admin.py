from django.contrib import admin
from briggs.models import * 
from django.forms import TextInput

# Register your models here.

def make_visible(modelAdmin, request, queryset):
	queryset.update(visible=True)

def make_invisible(modelAdmin, request, queryset):
	queryset.update(visible=False)

make_visible.short_description = "Mark selected quotes as visible"
make_invisible.short_description = "Mark selected quotes as invisible"


class BriggsQuoteAdmin(admin.ModelAdmin):
	fieldsets = [
		('Quote', {'fields': ['quote_text']}),
		('Misc',  {'fields': ['id', 'visible']}),
		('Votes', {'fields': ['votesPos', 'votesNeg'] }),
	]
	readonly_fields=('id',)

	formfield_overrides = {
		models.CharField: {'widget': TextInput(attrs={'size':'100'})}
	}

	list_display = ['quote_text', 'visible', 'id', 'votesPos', 'votesNeg']
	actions = [make_visible, make_invisible]


admin.site.register(BriggsQuote, BriggsQuoteAdmin)
admin.site.register(BriggsVote)
